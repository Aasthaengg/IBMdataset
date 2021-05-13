a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())
temp=[a1,a2,a3,b1,b2,b3]
t1=temp.count(1)
t2=temp.count(2)
t3=temp.count(3)
t4=temp.count(4)
if max(t1,t2,t3,t4)==2:
  print("YES")
else:
  print("NO")