a,b,c,d=map(int,input().split())

if b<=0 and c>=0:
  print(b*c)
  
elif a>=0 and d<=0:
  print(a*d)
  
elif d<=0 and b<=0 :
  print(c*a)
  
elif a>=0 and c>=0 :
  print(b*d)
  
else:
  print(max(a*c,b*d))