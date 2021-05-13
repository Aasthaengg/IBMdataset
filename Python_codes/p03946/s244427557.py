N, T = map(int, input().split())
A = list(map(int, input().split()))
m = A[0]
B = []
for i in range(1, N):
    m = min(m, A[i-1])
    B.append(A[i]-m)

M = max(B)
print(B.count(M))