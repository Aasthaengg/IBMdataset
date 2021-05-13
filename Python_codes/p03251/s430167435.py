n,m,X,Y=map(int, input().split())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
judge=0
for i in range(X+1, Y+1):
    xc=0
    yc=0
    for j in range(n):
        if x[j]<i:
            xc+=1
    for k in range(m):
        if y[k]>=i:
            yc+=1
    if xc==n and yc==m:
        judge+=1
        break
if judge==0:
    print("War")
else:
    print("No War")