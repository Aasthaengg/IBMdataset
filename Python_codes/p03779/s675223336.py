n = int(input())
ans = 0
for i in range(1, n + 1):
    if n <= i * (i + 1) // 2:
        ans = i
        break
print(ans)
