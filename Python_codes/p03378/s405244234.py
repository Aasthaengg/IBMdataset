n, m, x = map(int, input().split())
A = [0] * (n + 1)
for i in list(map(int, input().split())):
  A[i] = 1
print(min(sum(A[:x]), sum(A[x + 1:])))
