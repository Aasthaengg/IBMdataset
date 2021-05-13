#WIP
#print(1 or 3)
#print(1 and 3)
W,H,x,y=map(int,input().split())
print(W*H/2,'1' if W/2==x and H/2==y else '0')
