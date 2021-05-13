_, n = map(int,input().split())
itv = []
for i in range(n):
    a,b = map(int, input().split())
    itv.append([b, a])

itv.sort()

ans, x = 0, 0
for [b, a] in itv:
    if a > x:
        ans += 1
        x = b - 1

print(ans)
