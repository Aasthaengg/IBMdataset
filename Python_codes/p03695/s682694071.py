N = int(input())
a = list(map(int,input().split()))
color = [False]*8
over_human = 0
for i in a:
    if(i<=399):
        color[0]=True
    elif(i<=799):
        color[1]=True
    elif(i<=1199):
        color[2]=True
    elif(i<=1599):
        color[3]=True
    elif(i<=1999):
        color[4]=True
    elif(i<=2399):
        color[5]=True
    elif(i<=2799):
        color[6]=True
    elif(i<=3199):
        color[7]=True
    elif(i>=3200):
        over_human += 1
if(color.count(True)==0):
    print(1,color.count(True)+over_human)
else:
    print(color.count(True),color.count(True)+over_human)
