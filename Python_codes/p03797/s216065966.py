n,m = map(int,input().split())
ans = 0
if m < 2:
  print(0)
  exit()
if n >= 2*m:
  ans += n
elif 0 <= n <= m//2:
  ans += n
  ans += (m - 2*n)//4
else:
  ans += m//2
    
print(ans)