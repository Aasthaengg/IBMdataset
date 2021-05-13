n = int(input())

divisors = set()
for i in range(1, int(n**.5)+1):
    if n % i == 0:
        divisors |= {i, n//i}
ans = 0
for div in divisors:
    m = div-1
    if m <= n//div:
        continue
    ans += m
print(ans)
