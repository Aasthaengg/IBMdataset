N=int(input())
A=list(map(int,input().split()))
x=dict()
m=1
mc=0
ans=0
for i in range(N):
    if A[i] in x:
        x[A[i]]+=1
        m=max(m,x[A[i]])
        if m==x[A[i]]:
            mc=A[i]
    else:
        x[A[i]]=1
        ans+=1
if mc==0:
    print(N)
    exit()
l=[]
for idx in x:
    l.append(x[idx]-1)

n=sum(l)
if n%2==0:
    print(ans)
else:
    print(ans-1)