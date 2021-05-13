x = int(input())
ans = 1
for i in range(2, int(x ** 0.5) + 1):
    n = 1
    while n * i <= x:
        n *= i
    ans = max(ans, n)
print(ans)
