x,a,b=list(map(int,input().split()))
if (a-b)>=0:
    print("delicious")
elif (a-b)<0 and (x-(b-a))>=0:
    print("safe")
else:
    print("dangerous")
