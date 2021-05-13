N = int(input())
# A = list(map(int,input().split()))
A = [-1] + list(map(int,input().split()))
B = [0] * (N+1)
for i in range(N, 0, -1):
  tmp = 0
  for j in range(2*i, N+1, i):
    tmp += B[j]
  if tmp%2 != A[i]:
    B[i] = 1

print(B.count(1))
if B.count(1) > 0:
  print(" ".join(map(str, [ i for i,b in enumerate(B) if b==1 ])))