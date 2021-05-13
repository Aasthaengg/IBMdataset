n,x,y=map(int,input().split())
if (x+y)>n:
  mn=(x+y)-n
else:
  mn=0
mx=min(x,y)
print('{} {}'.format(mx,mn))