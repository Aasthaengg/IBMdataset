n,c,k=map(int,input().split())
T=[int(input()) for i in range(n)]
T.sort()
ans=0; now=0; nowc=0
for  ii in range(n):
    if now>=T[ii] and nowc<c: nowc+=1; continue
    now=T[ii]+k
    nowc=1
    ans+=1
print(ans)