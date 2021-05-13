H,W=map(int,input().split())

s=[]

for r in range(H):
    s.append(list(input()))

c=[[200]*W for i in range(H)]
if s[0][0]==".":
    c[0][0]=0
else:
    c[0][0]=1

def rec(y,x):
    if c[y][x]!=200:
        return c[y][x]
    elif y==0 and x!=0:
        temp=rec(y,x-1)
        if s[y][x]!=s[y][x-1]:
            if s[y][x]=="#":
                temp+=1
        c[y][x]=temp
        return temp
    elif y!=0 and x==0:
        temp=rec(y-1,x)
        if s[y][x]!=s[y-1][x]:
            if s[y][x]=="#":
                temp+=1
        c[y][x]=temp
        return temp
    else:
        temp1 = rec(y, x - 1)
        if s[y][x] != s[y][x-1]:
            if s[y][x] == "#":
                temp1 += 1
        temp2 = rec(y - 1, x)
        if s[y][x] != s[y - 1][x]:
            if s[y][x] == "#":
                temp2 += 1
        temp=min(temp1,temp2)
        c[y][x]=temp
        return temp

ans=rec(H-1,W-1)

print(ans)

