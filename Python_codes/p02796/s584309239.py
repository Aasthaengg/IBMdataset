n = int(input())
edge_ls = [0] * n
for i in range(n):
    x,l = map(int,input().split())
    r = x+l
    left = x-l
    edge_ls[i] = [left,r]
edge_ls.sort(key=lambda x : x[1])
ans = 1
last = edge_ls[0][1]
for i in range(1,n):
    if last <= edge_ls[i][0]:
        ans += 1
        last = edge_ls[i][1]
print(ans)
    



