n,a,b=map(int,input().split())
a_=a+b*(n-1)
b_=a*(n-1)+b
if n==1 and a!=b:
  print(0)
elif a>b:
  print(0)
else:
  print(a_-b_+1)