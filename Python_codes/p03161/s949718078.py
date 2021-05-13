n,k = map(int,input().split())
h_ls = list(map(int, input().split()))
mincost_ls = [float('inf')] * n
mincost_ls[0] = 0
for i in range(n):
    for j in range(1,k+1):
        if i+j < n:
            mincost_ls[i+j] = min(mincost_ls[i+j], mincost_ls[i] + abs(h_ls[i+j]-h_ls[i]))
print(mincost_ls[-1])

