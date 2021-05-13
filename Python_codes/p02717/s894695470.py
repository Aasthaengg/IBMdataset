x,y,z=map(int,input().split())

p=x
x=y
y=p

p=x
x=z
z=p

print('%s %s %s' %(x,y,z))