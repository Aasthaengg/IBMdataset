h,w=map(int,input().split())

s=[input() for _ in range(h)]

ans=[[0]*w for _ in range(h)]
for i in range(w):
    if s[0][i]=='#' :
        break
    ans[0][i]=1
for j in range(h):
    if s[j][0]=='#' :
        break
    ans[j][0]=1

for i in range(1,h):
    for j in range(1,w):
        if s[i][j]=='#':
            ans[i][j]=0
        else:
            ans[i][j]=ans[i][j-1]+ans[i-1][j]

print(ans[h-1][w-1]%(1000000000+7))

