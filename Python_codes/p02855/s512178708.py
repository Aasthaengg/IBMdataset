h,w,k=map(int,input().split())
s=[list(input()) for i in range(h)]
Sep=[]
f=0
for i in range(h-1):
    if f or "#" in s[i]:
        if "#" in s[i+1]:
            Sep.append(i+1)
        else:
            f=1
Sep.append(h)
now=0
ind=1
for x in range(len(Sep)):
    f=0
    for j in range(w):
        for i in range(now,Sep[x]):
            if s[i][j]=="#":
                f+=1
                if f>1:
                    ind+=1
                    for y in range(now,Sep[x]):
                        s[y][j]=ind
                    break
            s[i][j]=ind
    now=Sep[x]
    ind+=1
for i in s:
    print(*i)