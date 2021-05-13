vis = [0]*4

for i in range(3):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    vis[a] += 1
    vis[b] += 1

cnt1 = vis.count(1)
cnt2 = vis.count(2)

if cnt1 == 2 and cnt2 == 2:
    print("YES")
else:
    print("NO")