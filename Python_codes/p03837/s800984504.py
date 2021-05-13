Node,Path = map(int,input().split())
ad_mat = [[float('inf')]*Node for _ in range(Node)]
path_ls = [[0,0,0] for _ in range(Path)]
for i in range(Path):
    a,b,c = map(int,input().split())
    ad_mat[a-1][b-1] = c
    ad_mat[b-1][a-1] = c
    path_ls[i] = a-1,b-1,c
for i in range(Node):
    ad_mat[i][i] = 0

for stop in range(Node):
    for start in range(Node):
        for end in range(Node):
            ad_mat[start][end] = min(ad_mat[start][end],ad_mat[start][stop]+ad_mat[stop][end])

ans = 0
for a,b,cost in path_ls:
    if cost > ad_mat[a][b]:
        ans += 1
print(ans)