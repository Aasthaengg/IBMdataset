import bisect

def divisor(n):
    lower, upper = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
        i += 1
    return lower + upper[::-1]

n, m = map(int, input().split())
M = divisor(m)
if n not in M:
    x = bisect.bisect_left(M, n)
    ans = (m // M[x])
else:
    ans = m // n
print(ans)
