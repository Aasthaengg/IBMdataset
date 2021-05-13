a, b = map(int, input().split())
ans = 0

for i in range(1, a+1):
    if i + b - 1 <= a:
        ans = ans + 1

print(ans)
