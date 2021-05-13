W,H,x,y=map(int,input().split())
s=W*H/2
x=1 if W/2==x and H/2==y else 0
print('{} {}'.format(s,x))