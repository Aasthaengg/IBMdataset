H,W = map(int,input().split())
cost_mat = []
for i in range(10):
    cost_mat.append(list(map(int, input().split())))

for stop in range(10):
    for start in range(10):
        for end in range(10):
            cost_mat[start][end] = min(cost_mat[start][end], cost_mat[start][stop] + cost_mat[stop][end])
cost = 0
for h in range(H):
    in_ls = list(map(int, input().split()))
    for num in in_ls:
        if not num == -1:
            cost += cost_mat[num][1]
print(cost)