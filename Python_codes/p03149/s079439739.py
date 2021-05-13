n1,n2,n3,n4=map(int,input().split())
t=[n1,n2,n3,n4]
t.sort()
if t[0]==1 and t[1]==4 and t[2]==7 and t[3]==9:
  print("YES")
else:
  print("NO")