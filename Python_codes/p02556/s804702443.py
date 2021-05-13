n=int(input())

xy=[list(map(int,input().split())) for _ in range(n)]

xpy=[]
xmy=[]

for i in range(n):
    xpy.append(xy[i][0]+xy[i][1])
    xmy.append(xy[i][0]-xy[i][1])

xpy.sort()
xmy.sort()

print(max(abs(xpy[-1]-xpy[0]),abs(xmy[-1]-xmy[0])))
