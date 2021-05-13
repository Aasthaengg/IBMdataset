N = int(input())
A = input()
B = input()
C = input()
ans = 0
for i in range(N):
  X = []
  X.append(A[i])
  X.append(B[i])
  X.append(C[i])
  X = set(X)
  ans += len(X) - 1
  
print(ans)