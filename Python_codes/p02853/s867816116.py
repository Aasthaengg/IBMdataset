X,Y = map(int,input().split())
if X==Y==1:print(1000000)
elif X<=3and Y<=3:print(((4-X)+(4-Y))*10**5)
else:print((4-min(X,Y))*10**5if 4-(min(X,Y))>=0else 0)