x,y=map(int,input().split())
ans = 0
while True:
  if x > y:
    print(ans)
    break
  else:
    ans += 1
    x *= 2