n = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(n):
  ind = -1
  for j in range(len(A)):
    if A[j] == j + 1:
      ind = j
  if ind == -1:
    break
  else:
    A.pop(ind)
    ans.append(ind+1)

if ind == -1:
  print(-1)
else:
  ans.reverse()
  for a in ans:
    print(a)