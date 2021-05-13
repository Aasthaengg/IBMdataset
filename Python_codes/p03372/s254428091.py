n,c=map(int,input().split())
sushi=[]
for i in range(n):
    x,v=map(int,input().split())
    sushi.append([x,v])
sushi.sort()
cw=[0]
cw_s=[]
cw_sum=0
for i in range(n):
    x=sushi[i][0]
    v=sushi[i][1]
    cw_sum=cw_sum+v
    cw.append(max(cw[-1],cw_sum-x))
    cw_s.append(cw_sum-2*x)
acw=[0]
acw_s=[]
acw_sum=0
for i in range(n):
    x=c-sushi[n-1-i][0]
    v=sushi[n-1-i][1]
    acw_sum=acw_sum+v
    acw.append(max(acw[-1],acw_sum-x))
    acw_s.append(acw_sum-2*x)
ans=max(cw[n],acw[n])
for i in range(n):
    ans=max(ans,acw_s[i]+cw[n-1-i],cw_s[i]+acw[n-1-i])
print(ans)
