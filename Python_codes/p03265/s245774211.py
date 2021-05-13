x1,y1,x2,y2=map(int,input().split())

diff = x2-x1,y2-y1

x3,y3 = x2-diff[1],y2+diff[0]
x4,y4 = x1-diff[1],y1+diff[0]

print(*(x3,y3,x4,y4))