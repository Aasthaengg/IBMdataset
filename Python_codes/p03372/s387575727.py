n,c=map(int,input().split())

xv=[]
xv_rev=[]

for _ in range(n):
    x,v=map(int,input().split())
    xv.append((x,v))
    xv_rev.append((c-x,v))

xv_rev=xv_rev[::-1]

#(最大価値,その時の距離,累積価値合計,累積距離)

ittekoi=[0]*n
itte=[0]*n

sumv=0
#時計回り
for i,(x,v) in enumerate(xv):
    if i==0:
        sumv=v
        itte[i]=max(0,sumv-x)
        ittekoi[i]=max(0,sumv-2*x)
    else:
        sumv+=v
        itte[i]=max(itte[i-1],sumv-x)
        ittekoi[i]=max(ittekoi[i-1],sumv-2*x)    

sumv=0
ittekoi2=[0]*n
itte2=[0]*n

#班時計周り
for i,(x,v) in enumerate(xv_rev):
    if i==0:
        sumv=v
        itte2[i]=max(0,sumv-x)
        ittekoi2[i]=max(0,sumv-2*x)
    else:
        sumv+=v
        itte2[i]=max(itte2[i-1],sumv-x)
        ittekoi2[i]=max(ittekoi2[i],sumv-2*x)    

#print(itte,ittekoi)
#print(itte2,ittekoi2)

ans=0
for i in range(n):
    if i==n-1:
        ans=max(ans,itte[i])
        ans=max(ans,itte2[i])
    else:
        ans=max(ans,itte[i]+ittekoi2[n-i-2])
        ans=max(ans,itte2[i]+ittekoi[n-i-2])

print(ans)


        


