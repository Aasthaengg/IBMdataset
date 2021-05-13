N = int(input())

ST = []
for _ in range(N):
    x, l = map(int, input().split())
    ST.append((x-l, x+l))

ST.sort(key=lambda x: x[1])

ans = 0
cur = -1e9
for i in range(N):
    s, t = ST[i]
    if cur <= s:
        ans += 1
        cur = t
print(ans)
