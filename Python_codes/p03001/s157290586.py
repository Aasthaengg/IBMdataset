W,H,x,y=map(int,input().split())
if W/2==x and H/2==y:
 lst=[W*H/2,1]
else:
 lst=[W*H/2,0]
print(*lst)