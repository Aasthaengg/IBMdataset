a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())
l = [a,b,c,d,e,f]
if l.count(1)>=3:
  print("NO")
  exit()
if l.count(2)>=3:
  print("NO")
  exit()
if l.count(3)>=3:
  print("NO")
  exit()
if l.count(4)>=3:
  print("NO")
  exit()
print("YES")