n,a,b=map(int,input().split())
if a>b:a,b=b,a
if (a+b)%2:
  print(min(a+b-1,(n-a)+(n-b)+1)//2)
else:print((b-a)//2)