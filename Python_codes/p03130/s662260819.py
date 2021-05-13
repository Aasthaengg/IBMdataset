a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
li=[a,b,c,d,e,f]
x=[li.count(i) for i in range(1,5)]
if max(x)<3:
  print("YES")
else:
  print("NO")