N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

X=[0]*N
minus=0
ans=0
for i in range(N):
    X[i]=A[i]-B[i]
    if X[i]<0:
        ans+=1
        minus+= X[i]

X.sort(reverse=True)
if sum(X)<0:
    ans=-1
else:
    i=0
    while minus<0:
        minus+=X[i]
        i+=1
    ans+=i

print(ans)