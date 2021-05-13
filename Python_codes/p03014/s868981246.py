h,w=map(int,input().split())

s=[['#']*(w+2)]
for i in range(h):
    s.append(['#']+list(input())+['#'])
s.append([['#']*(w+2)])

l=[[0]*(w+2) for _ in range(h+2)]
r=[[0]*(w+2) for _ in range(h+2)]
u=[[0]*(w+2) for _ in range(h+2)]
d=[[0]*(w+2) for _ in range(h+2)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j]=='.':
            l[i][j]=l[i][j-1]+1
            u[i][j]=u[i-1][j]+1
        if s[i][w+1-j]=='.':
            r[i][w+1-j]=r[i][w+2-j]+1
        if s[h+1-i][j]=='.':
            d[h+1-i][j]=d[h+2-i][j]+1

ans=0
for i in range(1, h+1):  # hはy座標
    for j in range(1, w+1):  # wはx座標
        tmp_ans=l[i][j]+r[i][j]+u[i][j]+d[i][j]-3
        ans=max(ans, tmp_ans)
print(ans)
