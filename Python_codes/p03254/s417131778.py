N,X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
k1 = k2 = 0
for i in range (N):
  if sum(A[:i+1]) > X:
    k1 = i
    k2 = 1
    break
  elif sum(A) == X:
    k1 = N
    k2 = 1
    break
if k2 == 0:
  k1 = N - 1
print(k1)