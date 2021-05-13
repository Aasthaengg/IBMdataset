n, d = map(int, input().split())
ans = 0
while True:
  ans +=1
  n -= 2*d+1
  if n <= 0:
    print(ans)
    break
