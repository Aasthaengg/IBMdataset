h,a=map(int,input().split())
if h>a:
  if h%a==0:print(h//a)
  if h%a>0:print(h//a+1)
if h<=a:
  print(1)