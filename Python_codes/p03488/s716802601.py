import sys
input = sys.stdin.readline
s=list(input())
x,y = map(int, input().split())
y=abs(y)
s.append('T')
x1=[]
y1=[]

count=0
u=0
for i in range(len(s)):
    if s[i]=='F':
        count+=1
    else:
        if u%2==0:
            x1.append(count)
            u+=1
            count=0
        else:
            y1.append(count)
            u+=1
            count=0
v=sum(x1)
w=sum(y1)
v-=x1[0]
x-=x1[0]
x1.pop(0)
x=abs(x)
if v<x or w<y:
    print('No')
    exit()

dpx=[[0 for i in range(v+1)] for j in range(len(x1)+1)]
dpx[0][-1]=1

for i in range(len(x1)):
    for j in range(v+1):
        if dpx[i][j]==1:
            if j-2*x1[i]>=0:
                dpx[i+1][j-2*x1[i]]=1
            dpx[i+1][j]=1

if len(y1)==0:
    y1.append(0)
dpy=[[0 for i in range(w+1)] for j in range(len(y1)+1)]
dpy[0][-1]=1

for i in range(len(y1)):
    for j in range(w+1):
        if dpy[i][j]==1:
            if j-2*y1[i]>=0:
                dpy[i+1][j-2*y1[i]]=1
            dpy[i+1][j]=1

if dpy[-1][y]==1 and dpx[-1][x]==1:
    print('Yes')
else:
    print('No')
