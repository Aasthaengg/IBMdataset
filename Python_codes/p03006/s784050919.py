from collections import Counter
n = int(input())
XY = [list(map(int,input().split())) for _ in range(n)]
dXY = Counter([])
for i in range(n):
    for j in range(n):
        if i!=j:
            dXY += Counter([str(XY[i][0]-XY[j][0])+'_'+str(XY[i][1]-XY[j][1])])
if n==1:
    print(1)
else:
    print(n-dXY.most_common()[0][1])