
K, N = [int(n) for n in input().split(" ")]
A = [int(n) for n in input().split(" ")]

L = []
for i in range(N - 1):
    ll = A[i + 1] - A[i] 
    L.append(ll)
L.append(A[0] + K - A[-1])

LL = max(L)

print(K - LL)