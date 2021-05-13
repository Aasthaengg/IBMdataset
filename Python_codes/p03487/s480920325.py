N = int(input())
A = list(map(int, input().split()))
A.sort()
old = A[0]
ans = 0
a = 1
for i in range(1, N):
  if A[i] == old: 
    a += 1
  else:
    if old > a:
      ans += a
    elif old < a:
      ans += a - old
    old = A[i]
    a = 1
if old > a:
  ans += a
elif old < a:
  ans += a - old
print(ans)