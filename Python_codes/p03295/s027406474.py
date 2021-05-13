n_node, Q = map(int,input().split())
Q_ls = [[0,0] for _ in range(Q)]
for i in range(Q):
    a,b = map(int,input().split())
    Q_ls[i] = [a-1,b-1]
Q_ls.sort(key=lambda x: x[1])

last_r = -1
ans = 0
for i in range(Q):
    if Q_ls[i][1] > last_r and Q_ls[i][0] >= last_r:
        ans += 1
        last_r = Q_ls[i][1]
print(ans)
