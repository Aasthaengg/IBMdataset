n = int(input())
itv = []
for i in range(n):
    x,l = map(int, input().split())
    start = x - l if x - l > 0 else 0
    end = x + l
    itv.append([end, start])

itv.sort()

ans, t = 0, 0
for [x, l] in itv:
    if t <= l:
        ans += 1
        t = x

print(ans)
