n=int(input())
xbox=[]
ybox=[]
for i in range(n):
    x,y = map(int,input().split())
    xbox.append(x)
    ybox.append(y)
xmax=max(xbox)
xmin = min(xbox)
ymax=max(ybox)
ymin=min(ybox)
box1=[]
box2=[]
box3=[]
box4=[]
for i in range(n):
    box1.append(xmax+ymax-xbox[i]-ybox[i])
    box2.append(-xmin + ymax + xbox[i] - ybox[i])
    box3.append(xmax - ymax - xbox[i] + ybox[i])
    box4.append(-xmax - ymax + xbox[i] + ybox[i])
print(max([max(box1)-min(box1),max(box2)-min(box2),max(box3)-min(box3),max(box4)-min(box4)]))
