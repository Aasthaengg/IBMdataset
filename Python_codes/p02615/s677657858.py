N=int(input())
A=list(map(int,input().split()))

A.sort(reverse=True)

B=[]
B.append(A[0])
for i in range(1,N):
    B.append(A[i])
    B.append(A[i])

ans=0
for i in range(N-1):
    ans += B[i]

print(ans)