n,m = map(int,input().split())
ans = 0
if 2*n <= m:
  ans += n
  ans += (m-2*n)//4
  
else:
  ans += m//2
  
print(ans)