from itertools import permutations
n_node, n_edge, R = map(int,input().split())
r_ls = list(map(int,input().split()))
for i in range(R):
    r_ls[i] -= 1
ad_mat = [[float('inf')]*n_node for _ in range(n_node)]
for i in range(n_node):
    ad_mat[i][i] = 0
for i in range(n_edge):
    a,b,c = map(int,input().split())
    ad_mat[a-1][b-1] = c
    ad_mat[b-1][a-1] = c

# ワーシャルフロイド
for stop in range(n_node):
    for start in range(n_node):
        for end in range(n_node):
            ad_mat[start][end] = min(ad_mat[start][end],ad_mat[start][stop]+ad_mat[stop][end])

ans = float('inf')
for path in permutations(r_ls):
    cost = 0
    for i in range(R-1):
        cost += ad_mat[path[i]][path[i+1]]
    ans = min(ans,cost)
print(ans)
