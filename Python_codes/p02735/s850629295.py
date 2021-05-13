h,w=map(int,input().split())
s=list()
for i in range(h):
    line=str(input())
    s.append(line)


result=list()
for i in range(h):
    line=list()
    for j in range(w):
        line.append(0)
    result.append(line)
def se(x,y):
    if x==0 and y==0:
        if s[0][0]=="#":
            result[x][y]=1
        else:
            result[x][y]=0
    elif x==0:
        if s[x][y-1]!=s[x][y]:
            result[x][y]=result[x][y-1]+1
        else:
            result[x][y]=result[x][y-1]
    elif y==0:
        if s[x-1][y]!=s[x][y]:
            result[x][y]=result[x-1][y]+1
        else:
            result[x][y]=result[x-1][y]
    else:
        if s[x][y-1]!=s[x][y]:
            a=result[x][y-1]+1
        else:
            a=result[x][y-1]
        if s[x-1][y]!=s[x][y]:
            b=result[x-1][y]+1
        else:
            b=result[x-1][y]
        result[x][y]=min(a,b)
        
for i in range(h):
    for j in range(w):
        se(i,j)
        
if s[h-1][w-1]=="#":
    result[h-1][w-1]+=1
else:
    pass


print(int(result[h-1][w-1]/2))