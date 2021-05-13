N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
ans = 0
for i in reversed(range(N)):
  mod = (A[i][0] + ans) % A[i][1]
  if mod != 0:
    ans += A[i][1] - mod
print(ans)