import copy
loss=0
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
def warshall_floyd2(d):
    #d[i][j]: iからjへの最短距離
    ans=0
    for i in range(n):
        for j in range(n):
            flg=0
            for k in range(n):
                if i==j or j==k or k==i:
                    continue
                if d[i][j]==d[i][k] + d[k][j]:
                    flg=1
            if flg==0:
                ans+=d[i][j]
    #print(loss)
    return ans

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
b=copy.deepcopy(a)
b=warshall_floyd(b)
#print(a)
#print(b)
flg=True
for i in range(n):
    for j in range(n):
        if a[i][j]!=b[i][j]:
            flg=False
            break
    else:
        continue
    break
if flg:
    ans=warshall_floyd2(b)
    print(ans//2)
else:
    print(-1)
