s=input()
X,Y=map(int,input().split())
from collections import defaultdict
def solve(a,dp,G):
    for i in range(len(a)):
        tmp=set()
        for j in dp:
            tmp.add(j-a[i])
            tmp.add(j+a[i])
        dp=tmp
    if G in dp:
        return True
    else:
        return False

d=[len(x) for x in s.split("T")]
#print(d)
x=d[2::2]
dpx={d[0]}
y=d[1::2]
dpy={0}
if solve(x,dpx,X) and solve(y,dpy,Y):
    print("Yes")
else:
    print("No")
