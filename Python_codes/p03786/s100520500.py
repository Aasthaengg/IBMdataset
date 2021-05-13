N=int(input())
A=list(map(int,input().split()))
A.sort()
S=[0]
for i in range(N):
    S.append(S[i]+A[i])

lose=0
for i in range(N-1):
    if S[i+1]*2<A[i+1]:
        lose=i+1
print(N-lose)