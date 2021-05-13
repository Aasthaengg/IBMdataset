A, B, K = map(int, input().split())
f = 0
for i in range(K):
  if f == 0:
    A, B = A // 2, B + A // 2
  else:
    A, B = A + B // 2, B // 2
  f ^= 1
print(str(A) + " " + str(B))