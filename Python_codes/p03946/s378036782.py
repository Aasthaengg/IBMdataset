n, t = map(int, input().split())
A = list(map(int, input().split()))
B = [-1]*n
B[-1] = A[-1]
for i in range(n-2, 0, -1):
  B[i] = max(A[i], B[i+1])
L = [B[i+1]-A[i] for i in range(n-1)]
ans = L.count(max(L))
print(ans)