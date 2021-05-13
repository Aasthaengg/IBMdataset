a,b,c=map(int,input().split())
d=max(a,b,c)
if a%2==0 or b%2==0 or c%2==0:
  print(0)
elif a%2==1 and b%2==1 and c%2==1 and d==a:
  print(b*c)
elif a%2==1 and b%2==1 and c%2==1 and d==b:
  print(a*c)
elif a%2==1 and b%2==1 and c%2==1 and d==c:
  print(b*a)