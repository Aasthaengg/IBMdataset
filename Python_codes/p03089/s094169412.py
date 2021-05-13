N = int(input())
B = list(map(int,input().split()))
l = len(B)
A = []
ans = -1
for i in range(N):
  max_j = -1
  for j in range(N-i):
    if B[j] == j+1:
      max_j = j
  if (max_j == -1):
    break
  else:
    A.append(B.pop(max_j))
if (l == len(A)):
  for i in reversed(A):
    print(i)
else:
  print(ans)