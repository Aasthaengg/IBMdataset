w,a,b = map(int,input().split())
 
x = b-(a+w)
y = a-(b+w)
 
if a<=b<=a+w:
  print(0)
else:
  ans = min(abs(x),abs(y))
  print(ans)