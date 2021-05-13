N=int(input())
S=[]
T=[]
for i in range(N):
    s,t=map(str,input().split())
    S.append(s)
    T.append(int(t))
X=input()

f=S.index(X)
ans=0
if f==N-1:
    print(0)
else:
    for i in range(f+1,N):
        ans+=T[i]
    print(ans)