n,m,c=map(int,input().split())
base = list(map(int,input().split()))
x=[list(map(int, input().split())) for i in range(n)]
ans=0
cnt=0
for i in range(n):
    cnt=0
    for k in range(m):
        cnt+=base[k]*x[i][k]
    cnt+=c
    if cnt>0:
        ans+=1
    #←これがないとWAになるにゃ
print(ans)