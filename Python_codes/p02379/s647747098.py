val=list(map(float,input().split()))
if(val[0]>val[2]):
    x=(val[0]-val[2])**2
else:
    x=(val[2]-val[0])**2
if(val[1]>val[3]):
    y=(val[1]-val[3])**2
else:
    y=(val[3]-val[1])**2
    
length=(x+y)**0.5
print(length)
