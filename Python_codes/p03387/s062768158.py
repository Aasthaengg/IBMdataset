A = list(map(int, input().split()))
A.sort()
ans = A[2] - A[1]
a = A[1] - A[0]
if a % 2 == 0:
  ans += a // 2
else:
  ans += (a // 2) + 2
print(ans)