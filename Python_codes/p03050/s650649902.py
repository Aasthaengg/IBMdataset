n = int(input())
ans = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        k = (n // i) - 1
        if k > i:
            ans += k
print(ans)