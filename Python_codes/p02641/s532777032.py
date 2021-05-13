x, n = map(int, input().split())
p = set(map(int, input().split()))

ans = 1000
for i in range(102):
    if i not in p:
        ans = min(ans, abs(x - i))
print(x + ans if x - ans in p else x - ans)
