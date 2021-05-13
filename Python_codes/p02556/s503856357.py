N = int(input())
p1, p2, p3, p4 = [[10**9, 10**9], [0, 0], [0, 10**9], [10**9, 0]]
ans = 0
for i in range(N):
    x, y = map(int, input().split())
    if p1[0] + p1[1] >= x + y:
        p1 = [x, y]
    if p2[0] + p2[1] <= x + y:
        p2 = [x, y]
    if p3[0] - p3[1] <= x - y:
        p3 = [x, y]
    if p4[0] - p4[1] >= x - y:
        p4 = [x, y]
P = [p1, p2, p3, p4]
for x1, y1 in P:
    for x2, y2 in P:
        ans = max(ans, abs(x1-x2)+abs(y1-y2))
print(ans)
