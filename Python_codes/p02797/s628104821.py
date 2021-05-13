N, K, S = map(int, input().split())

A = [0]*N

for i in range(K):
    A[i] = S
    
for j in range(K, N):
    if(S+j+1 >= 10**9):
        A[j] = 1    
    else:
        A[j] = S+j+1
    
print(*A)