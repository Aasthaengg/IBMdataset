N, K = map(int, input().split())
A = list(map(int, input().split()))

N_0 = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] > A[j]:
            N_0 += 1
            
N_1 = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i] < A[j]:
            N_1 += 1
            
ans = N_0*(K*(K+1)//2) + N_1*((K-1)*K//2)
print(ans % (10**9+7))