n = int(input())
h_ls = list(map(int, input().split()))
mincost_ls = [float('inf')] * n
mincost_ls[0] = 0
for i in range(n-1):
    mincost_ls[i+1] = min(mincost_ls[i+1], mincost_ls[i]+abs(h_ls[i+1]-h_ls[i]))
    if i+2 < n:
        mincost_ls[i+2] = min(mincost_ls[i+2], mincost_ls[i]+abs(h_ls[i+2]-h_ls[i]))
print(mincost_ls[-1])