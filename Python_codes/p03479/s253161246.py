X, Y = map(int,input().split())

ans = 1

while 1:
  X *= 2
  if X <= Y:
    ans += 1
  else:
    print(ans)
    break