N=int(input())
A=[]
B=[]
for i in range(N):
    AB=list(map(int,input().split()))
    A.append(AB[0])
    B.append(AB[1])

ans=0
for i in range(N-1,-1,-1):
    A[i]+=ans
    A[i]%=B[i]
    if A[i]!=0:
        ans+=B[i]-A[i]

print(ans)