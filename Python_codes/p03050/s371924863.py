n = int(input())

divisors = set()

for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n//i)

ans = 0

for d in divisors:
    m = d-1
    if m != 0 and n//m == n % m:
        ans += m

print(ans)
