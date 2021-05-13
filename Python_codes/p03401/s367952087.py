N=int(input())
A=[0]
a=list(map(int,input().split()))
a.append(0)
A.extend(a)

res=0

for i in range(1,N+2):
    res+=abs(A[i-1]-A[i])

for i in range(1,N+1):
    print(res+abs(A[i-1]-A[i+1])-(abs(A[i]-A[i-1])+abs(A[i]-A[i+1])))