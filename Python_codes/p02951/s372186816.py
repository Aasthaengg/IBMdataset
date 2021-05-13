a,b,c = map(int,input().split())
 
if (a-b) <= c:
  print(str(c - (a - b)))
else:
  print("0")