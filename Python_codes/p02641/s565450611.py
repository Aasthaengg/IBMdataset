x, n = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
ans = 0
for i in range(102):
    if i in p:
        pass
    elif abs(x - ans) > abs(x - i):
        ans = i
print(ans)