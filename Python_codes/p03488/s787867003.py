from collections import deque
s=list(input())
x,y=map(int,input().split())
#print(s,x,y)
i=0
xflag=1
flag=0
xax=deque()
yax=deque()
cnt=0
while i<len(s):
    if s[i]=="F":
        cnt=cnt+1
    else:
        if cnt!=0:
            if xflag==1:
                xax.append(cnt)
            else:
                yax.append(cnt)
        xflag=(xflag+1)%2
        cnt=0
    i=i+1
if cnt!=0:
    if xflag == 1:
        xax.append(cnt)
    else:
        yax.append(cnt)
#print(xax,yax)
xdeq=deque()
ydeq=deque()
if (len(xax)>0)and(s[0]=="F"):
    x0=xax.popleft()
    xdeq.append(x0)
else:
    xdeq.append(0)
ydeq.append(0)
#print(xdeq,xax)
while len(xax)>0:
    subadd=xax.popleft()
    xdeq2=[]
    while len(xdeq)>0:
        xd=xdeq.popleft()
        xdeq2.append(xd-subadd)
        xdeq2.append(xd+subadd)
    xdeq2=list(set(xdeq2))
    for i in xdeq2:
        xdeq.append(i)
    #print(xdeq)
#print(xdeq)
while len(yax)>0:
    subadd=yax.popleft()
    ydeq2=[]
    while len(ydeq)>0:
        yd=ydeq.popleft()
        ydeq2.append(yd-subadd)
        ydeq2.append(yd+subadd)
    ydeq2=list(set(ydeq2))
    for i in ydeq2:
        ydeq.append(i)
    #print(ydeq)
#print(ydeq)
xlist=list(xdeq)
ylist=list(ydeq)
for i in xlist:
    for j in ylist:
        if (i==x)and(j==y):
            flag=1
            break
    if flag==1:
        break
if flag==1:
    print("Yes")
else:
    print("No")





