h,w=map(int,input().split())
s=[input() for i in range(h)]
res=True
a=[0,-1,1,0]
b=[-1,0,0,1]
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            continue
        else:
            res=False
            for k in range(4):
                if 0<=a[k]+i<h and 0<=b[k]+j<w:
                    if s[a[k]+i][b[k]+j]=="#":
                        res=True
        if not res:
            break
    if not res:
        break

if res:
    print("Yes")
else:
    print("No")
