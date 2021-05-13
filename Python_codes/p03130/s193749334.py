a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
L=[a,b,c,d,e,f]
R=set(L)
if len(R)==4 and L.count(1)<3 and L.count(4)<3 and L.count(3)<3 and L.count(2)<3:
  print("YES")
else:
  print("NO")