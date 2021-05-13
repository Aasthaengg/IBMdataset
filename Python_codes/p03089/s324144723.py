n= int(input())
b= list(map(int,input().split()))
getnum = []
while len(b)>0:
    tempmax=-1
    for i,c in enumerate(b):
        if i+1==c:tempmax=i
    if tempmax==-1:
        print(-1)
        break
    else:
        getnum.append(b[tempmax])
        del b[tempmax]
else:
    for t in getnum[::-1]:print(t)