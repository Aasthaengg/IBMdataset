s = input()
gx,gy = map(int, input().split())

x_lis=[]
y_lis=[]

cnt=0
now="x"
for i in range(len(s)):
    if s[i]=="F":
        cnt+=1
    else:
        if now=="x":
            x_lis.append(cnt)
            now="y"
        else:
            y_lis.append(cnt)
            now="x"
        cnt=0

if now=="x":
    x_lis.append(cnt)
    now="y"
else:
    y_lis.append(cnt)
    now="x"

now=set([0])
for i in range(len(x_lis)):
    nxt=set()
    for itm in now:
        nxt.add(itm + x_lis[i])
        if i!=0:
            nxt.add(itm - x_lis[i])
    now=nxt

if not gx in now:
    print("No")
    exit()

now=set([0])
for i in range(len(y_lis)):
    nxt=set()
    for itm in now:
        nxt.add(itm + y_lis[i])
        nxt.add(itm - y_lis[i])
    now=nxt

if not gy in now:
    print("No")
else:
    print("Yes")