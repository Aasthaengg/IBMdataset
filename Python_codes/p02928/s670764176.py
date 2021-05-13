N, K = map(int, input().split())
A = [int(i) for i in input().split()]

MOD = 10**9 + 7


B = [0] * N

for i in range(len(A)-1):
    cnt = 0
    for j in range(i+1, len(A)):
        if A[j] < A[i]:
            cnt += 1
    B[i] = cnt
# print(B)


C = [0] * N

for i in range(len(A)):
    cnt = 0
    for j in range(len(A)):
        if j != i:
            if A[i] > A[j]:
                cnt += 1
    C[i] = cnt
# print(C)    

D = []
for i in range(N):
    tmp = B[i] * K + C[i] * K * (K-1) // 2 
    D.append(tmp % MOD)
print(sum(D)% MOD)