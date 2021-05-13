def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


N = int(input())
d = make_divisors(N)
ans = 0
for i in d:
    a = i-1
    m = N//i
    if a > m:
        ans += a

print(ans)
