def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
n, m  = map(int, input().split())
divs = make_divisors(m)
divs.sort()
ans = 0
for d in divs:
    if m // d >= n:
        ans = d
print(ans)