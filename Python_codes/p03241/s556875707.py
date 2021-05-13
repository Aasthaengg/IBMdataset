n, m = map(int, input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

d = make_divisors(m)
ans = -1
for i in d:
    j = m//i
    if j >= n:
        ans = max(i, ans)
print(ans)
