N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

res = 0
for i, a in enumerate(A):
  res += B[a-1]
  if i != N-1:
    if A[i+1] == a + 1:
      res += C[a-1]

print(res)