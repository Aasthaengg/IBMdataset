x = int(input())
sm=0
res=0
for i in range(1,x+1):
    sm = (i+1)*i/2
    if sm>=x:
        res=i
        break
if sm-x==res:
    print(res-1)
else:
    print(res)