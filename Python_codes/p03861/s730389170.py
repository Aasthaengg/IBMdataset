a,b,x = map(int,input().split())
a_n = a // x
a_p = a % x
b_n = b // x

ans = b_n - a_n
if a_p == 0:
  print(ans+1)
else:
  print(ans)
