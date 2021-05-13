n = int(input())

multiplier = [0 for _ in range(n)]
for m in range(2, n+1):
    a = m
    i = 2
    while i ** 2 <= m:
        while a % i == 0:
            a = int(a / i)
            multiplier[i-1] += 1
        i += 1
    if a != 1:
        multiplier[a-1] += 1
ans = 1
for x in multiplier:
    ans *= x + 1
print(ans % (10**9 + 7))