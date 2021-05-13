N,K,S = map(int,input().split())
A = [S for _ in range(N)]
if S<10**9:
    for i in range(K,N):
        A[i]=10**9
else:
    for i in range(K,N):
        A[i] = 1
print(*A)