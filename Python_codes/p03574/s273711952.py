h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
a=[-1,0,1]
b=[-1,0,1]
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            s[i][j]=0
            for c in a:
                for d in b:
                    if i+c<0 or j+d<0 or i+c>h-1 or j+d>w-1 or (a==0 and b==0) or s[i+c][j+d]!="#":
                        continue
                    else:
                        s[i][j]+=1
for i in range(h):
    print(*s[i][:],sep="")