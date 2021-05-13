N = int(input())
A = [int(input()) for _ in range(N)]

if A[0] != 0:
  print(-1)
  exit()
  
ans = []
l = 0
for i in range(1, N):
  if A[i] > A[i - 1] + 1:
    print(-1)
    exit()
    
  if A[i] == A[i - 1] + 1:
    l = A[i]
  else:
    ans.append(l)
    l = A[i]
ans.append(l)
print(sum(ans))