import math
a=[]
while True:
    tmp=int(input())
    if tmp==0:
        break
    tmp1=[]
    tmp1.append(tmp)
    tmp1.append(list(map(int,input().split(" "))))
    a.append(tmp1)
for i in a:
    ave=sum(i[1])/i[0]
    sgm=math.sqrt(sum([(i[1][j]-ave)**2 for j in range(i[0])])/i[0])
    print(sgm)
