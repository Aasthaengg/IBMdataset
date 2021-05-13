h,w,a,b=map(int,input().split())
l=[[0]*w for _ in range(h)]
for i in range(h):
    if i<b:
        for j in range(a):
            l[i][j]=1
    else:
        for j in range(a,w):
            l[i][j]=1
for i in range(h):
    print("".join(str(n) for n in l[i]))