R,G,B,N=map(int,input().split())
cnt=0
for r in range(0,N+1):#N//R+1):
    for g in range(0,N+1):#(N-r*R)//G+1):
        bunshi=N-r*R-g*G
        q,m=divmod(bunshi,B)
        if q<0:continue
        if m==0:cnt+=1
            
print(cnt)