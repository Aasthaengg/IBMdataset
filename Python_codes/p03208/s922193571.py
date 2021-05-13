N, K = map(int, input().split())
A=[0]*N
for i in range(N):
    a=int(input())
    A[i]=a
A=sorted(A)

ans=[]
for i in range(N-K+1):
    ans.append(A[i+K-1]-A[i])

print(min(ans))