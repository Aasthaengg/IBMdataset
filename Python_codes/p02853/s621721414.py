x,y=map(int,input().split())
if x==y==1:print(10**6)
else:print((max(0,4-x)+max(0,4-y))*10**5)