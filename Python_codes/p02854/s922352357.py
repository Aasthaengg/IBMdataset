N=int(input())
A=list(map(int,input().split()))
left = 0
right = sum(A)
ans = 0

for i in range(N-1):
  left += A[i]
  right -= A[i]
  sa = abs(left-right)
  if i == 0:
    ans = sa
  elif ans > sa:
    ans = sa

print(ans)