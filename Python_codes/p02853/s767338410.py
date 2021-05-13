x,y=map(int,input().split())
c=0
c += max(4-x,0)*100000
c += max(4-y,0)*100000
if x*y == 1:
  c+=400000
print(c)