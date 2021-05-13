N = int(input())
c = 0
A = []
for i in range(N):
  a = int(input())
  if a > i:
    c = 1
  if i >=1 and a > A[i-1]+1:
    c = 1
  A.append(a)

ans = 0
if c == 1:
  ans = -1
else:
  for i in range(1,N):
    if A[i] == A[i-1]+1:
      if i == N-1:
        ans += A[i]
      continue
    else:
      ans += A[i-1]  
      if i == N-1:
        ans += A[i]
      continue      
print(ans)  