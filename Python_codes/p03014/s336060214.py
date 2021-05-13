h,w=map(int, input().split())
maps=[[0]*w for i in range(h)]
for i in range(h):
    s=input()
    for j in range(w):
        if s[j]=="#":
            maps[i][j]=-1
    
maps_l=[[0]*w for i in range(h)]
maps_r=[[0]*w for i in range(h)]
maps_u=[[0]*w for i in range(h)]
maps_d=[[0]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        if maps[i][j]==-1:
            maps_l[i][j]=0
        elif j==0:
            maps_l[i][j]=1
        else:
            maps_l[i][j]=maps_l[i][j-1]+1

for i in range(h):
    for j in range(w-1,-1,-1):
        if maps[i][j]==-1:
            maps_r[i][j]=0
        elif j==w-1:
            maps_r[i][j]=1
        else:
            maps_r[i][j]=maps_r[i][j+1]+1

for j in range(w):
    for i in range(h):
        if maps[i][j]==-1:
            maps_d[i][j]=0
        elif i==0:
            maps_d[i][j]=1
        else:
            maps_d[i][j]=maps_d[i-1][j]+1

for j in range(w):
    for i in range(h-1,-1,-1):
        if maps[i][j]==-1:
            maps_u[i][j]=0
        elif i==h-1:
            maps_u[i][j]=1
        else:
            maps_u[i][j]=maps_u[i+1][j]+1
ans=0
for i in range(h):
    for j in range(w):
        if maps[i][j]!=-1:
            ans=max(ans,maps_u[i][j]+maps_d[i][j]+maps_r[i][j]+maps_l[i][j]-3)

print(ans)