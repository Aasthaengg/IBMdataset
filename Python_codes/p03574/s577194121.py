h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
t=[["$"]*(w+2) for i in range(h+2)]
for i in range(h):
    for j in range(w):
        t[i+1][j+1]=s[i][j]
v=[1,0,-1]
for i in range(h):
    for j in range(w):
        cnt=0
        if t[i+1][j+1]==".":
            for k in v:
                for l in v:
                    if t[i+1+k][j+1+l]=="#":
                        cnt+=1
            t[i+1][j+1]=str(cnt)
for i in range(h+2):
    t[i]="".join(t[i])
for i in range(1,h+1):
    print(t[i][1:w+1])