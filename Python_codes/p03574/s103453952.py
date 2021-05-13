h,w=map(int,input().split())
s=[]
t=[(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
for i in range(h):
    s.append(list(input()))
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            tmp=0
            for x,y in t:
                if 0<=i+x<=h-1 and 0<=j+y<=w-1:
                    if s[i+x][j+y]=="#":
                        tmp+=1
            s[i][j]=str(tmp)
for i in range(h):
    print("".join(s[i]))