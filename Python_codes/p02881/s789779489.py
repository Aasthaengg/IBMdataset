n = int(input())
ans = (0, n)
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        ans = min(ans, (i, n // i), key=lambda x: abs(x[0] - x[1]))
print(ans[0] - 1 + ans[1] - 1)