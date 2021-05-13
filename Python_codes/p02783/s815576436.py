h , a = map(int,input().split())
ans = 0
while 1 :
  h -= a
  ans += 1
  if h <= 0 :
    break
print(ans)
