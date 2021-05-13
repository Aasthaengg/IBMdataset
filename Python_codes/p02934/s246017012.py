N = int(input())
A = list(map(int, input().split()))

A_inv = [1]*N

for i in range(N):
    A_inv[i] = 1/A[i]
    
ans = 1/sum(A_inv)
print(ans)