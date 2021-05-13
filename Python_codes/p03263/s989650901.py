h,w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int,input().split())))
now="R"
x,y=0,0
carry=False
ans=[]
while True:
    if carry:
        if a[y][x]%2==1: # drop
            carry=False
    else:
        if a[y][x]%2==1: # grab
            carry=True

    if now=="R":
        nxtx=x+1
        nxty=y
        if nxtx==w:
            nxtx=x
            nxty+=1
            now="L"
            if nxty==h:
                break
    else:
        nxtx=x-1
        nxty=y
        if nxtx==-1:
            nxtx=0
            nxty+=1
            now="R"
            if nxty==h:
                break
    if carry:
        ans.append([y+1,x+1,nxty+1,nxtx+1])
    x=nxtx
    y=nxty


print(len(ans))
for a in ans:
    print(*a)