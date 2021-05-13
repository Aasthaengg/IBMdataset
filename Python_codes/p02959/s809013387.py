N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans=0

for i in range (N):
    ans+=min(A[N-i],B[N-1-i])
    if  B[N-i-1]>A[N-i]:
        ans+=min(A[N-i-1],B[N-1-i]-A[N-i])
        A[N-i-1]-=min(A[N-i-1],B[N-1-i]-A[N-i])

print(ans)