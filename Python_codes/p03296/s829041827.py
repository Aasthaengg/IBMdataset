N = int(input())
A = list(map(int, input().split()))
L = [0]
for i in range(N-1):
  if A[i] != A[i+1]:
    L.append(i+1)
L.append(N)
S = 0
for i in range(len(L)-1):
  S += (L[i+1] - L[i]) // 2
print(S)