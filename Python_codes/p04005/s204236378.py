a,b,c = map(int,input().split())
ans = 0

if a%2 == 0 or b%2==0 or c%2==0:
  pass
  
else:
  ans += min(a*b,a*c,b*c)
print(ans)  