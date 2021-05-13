a,b = map(int,(input().split()))
ans=0

if a<=9 and b<=9:
  ans += a*b
  print(ans)
else:
  print(-1)