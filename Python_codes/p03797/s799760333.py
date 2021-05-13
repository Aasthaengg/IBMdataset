n, m = map(int,input().split())
ans = 0
if n*2 > m:
  if m%2 == 0:
    ans = m//2
  else:
    ans = (m-1)//2
else:
  ans += n
  m -= n*2
  ans += m//4
print(ans)