AA, BB, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = min(A) + min(B)
for i in range(M):
  x, y, c = list(map(int, input().split()))
  x-=1
  y-=1
  discount = A[x] + B[y] - c
  if discount < res:
    res = discount

print(res)
