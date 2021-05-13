a, b = input().split()
n = int(a + b)
ans = "Yes" if n == int(n ** 0.5) ** 2 else "No"
print(ans)
