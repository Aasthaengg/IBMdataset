n = int(input())
ans = 0
sqrt = int(n ** 0.5)
for i in range(1, sqrt+1):
    if n % i == 0:
        m = n // i - 1
        if m != 0 and n // m == n % m:
            ans += m
        if n // i == i: continue
        m = i - 1
        if m != 0 and n // m == n % m:
            ans += m
print(ans)