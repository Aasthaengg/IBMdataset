H, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = A[:N]
s = sum(A)
ans = 'No'
if s >= H:
  ans = 'Yes'
print(ans)