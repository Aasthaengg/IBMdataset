N,T=map(int, input().split())
A=list(map(int, input().split()))
L=[]
for i in range(N):
    if i==0:
        now=A[i]
        nowmax=now
    if now>A[i]:
        L.append(nowmax-now)
        now=A[i]
        nowmax=now
    else:
        nowmax=max(nowmax,A[i])
    if i==N-1:
        L.append(nowmax-now)
MAX=max(L)
ans=0
#print(L)
for l in L:
    if l==MAX:
        ans+=1
print(ans)