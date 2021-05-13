h,w=map(int,input().split())
m=[list(map(int,input().split())) for i in range(h)]
pre=0
ans=0
ret=[]
l=[[0,w,1],[w-1,-1,-1]]
for i in range(h):
    a,s,d=l[i%2]
    for j in range(a,s,d):
        if (pre+m[i][j])%2:
            pre=1
            x,y=(i,j+d) if 0<=j+d<=w-1 else (i+1,j) 
            if 0<=x<h and 0<=y<w:
              ans+=1
              ret.append([i+1,j+1,x+1,y+1])
        else:pre=0
print(ans)
for g in range(ans):
    print(*ret[g])
