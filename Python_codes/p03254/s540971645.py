N,x = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(N):
  if A[i] <= x:
    if i == N-1:
      if x == A[i]:
        ans += 1
    else:
      x -= A[i]
      ans += 1
  else:
    break
print(ans)
