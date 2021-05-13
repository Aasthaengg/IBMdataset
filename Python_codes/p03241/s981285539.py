N, M = list(map(int,input().split()))

def divisor(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if n % n//i == 0:
                res.append(n//i)

    res.sort()
    return res

d = divisor(M)
ans = 1
for x in d:
    m = M
    m -= x * (N - 1)
    if m > 0 and m % x == 0:
        ans = x

print(ans)
