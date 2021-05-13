w,a,b = map(int,input().split())

if a < b:
  if b-(a+w) >0:
    print(b-(a+w))
  else:
    print(0)
    
elif a==b:
  print(0)
  
elif a>b:
  if a-(b+w) >0:
    print(a-(b+w))
  else:
    print(0)
  
