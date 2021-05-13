n, h, w = map(int, input().split())
al, bl = [], []
for _ in range(n):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)

ans = 0
for a, b in zip(al, bl):
    if a >= h and b >= w:
        ans += 1
print(ans)