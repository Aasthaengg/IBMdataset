N = int(input())
A = list(map(int,input().split()))
A.sort()
S = A[0]
ind=0
for i in range(1,N):
    if A[i]>2*S:
        ind=i
    S+=A[i]
print(N-ind)
