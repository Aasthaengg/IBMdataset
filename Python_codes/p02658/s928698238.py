N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 1
max_limit = 10 ** 18
for i in range(N):
  ans *= A[i]
  if ans > max_limit:
    ans = -1
    break

if ans > max_limit:
  print(str(-1))
else:
  print(str(ans))