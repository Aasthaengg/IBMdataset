K,N = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

B = [0]*N
for i in range(N-1):
    B[i] = A[i+1] - A[i]
B[N-1] = A[0]+(K-A[N-1])

print(sum(B) - max(B))
