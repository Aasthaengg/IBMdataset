s=[len(c) for c in list(input().split("T"))]
x,y=map(int,input().split())
XX=s[::2]
YY=s[1::2]
X=set([XX[0]])
Y=set([0])
XXX=[]
for i in range(1,len(XX)):
    for j in X:
        XXX.append(j+XX[i])
        XXX.append(j-XX[i])
    X=set(XXX)
    XXX=[]

YYY=[]
for i in range(len(YY)):
    for j in Y:
        YYY.append(j+YY[i])
        YYY.append(j-YY[i])
    Y=set(YYY)
    YYY=[]

if x in X and y in Y:
    print("Yes")
else:
    print("No")