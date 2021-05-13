x,y = map(int,input().split())
if x==1 and y==1:
    print(1000000)
else:
    print(100000*(max(4-x,0)+max(4-y,0)))