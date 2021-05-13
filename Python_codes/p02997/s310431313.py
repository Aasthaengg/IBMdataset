n, k = map(int, input().split())

# 距離2の頂点対の数の最大値
mx = (n-1)*(n-2)//2

if k > mx:
    print(-1)
    exit()

ans = []
for i in range(1, n):
    ans.append((i, n))

add_edge = mx - k
edge = []
for i in range(1, n-1):
    for j in range(i+1, n):
        edge.append((i, j))

for i in range(add_edge):
    ans.append(edge[i])

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])