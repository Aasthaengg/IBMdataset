N = int(input())
x = [list(map(int, input().split())) for i in range(N)]
ans = 0
for i in range(N):
  a = x[N-i-1][0]
  b = x[N-i-1][1]
  c = b - (a % b)
  if a % b == 0:
    c = 0
  if ans <= c:
    ans = c
  elif (ans - c) % b != 0:
      n = (ans - c) // b
      ans = (n+1)*b + c
print(ans)