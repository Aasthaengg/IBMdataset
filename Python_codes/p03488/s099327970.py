def cango(l,x):
    n=sum(l)
    if abs(x)>n:
        return False
    dp=[False]*(n+1)
    dp[0]=True
    for i in range(len(l)):
        dp1=[False]*(n+1)
        for j in range(n+1):
            if dp[j]:
                dp1[abs(j-l[i])]=True
                dp1[j+l[i]]=True
        for i in range(n+1):
            dp[i]=dp1[i]
    return dp[abs(x)]

l=eval("['"+input().replace('T',"','")+"']")
for i in range(len(l)):
    l[i]=len(l[i])
x,y=map(int,input().split())
if len(l)==1:
    print(['No','Yes'][x==l[0] and y==0])
elif len(l)==2:
    print(['No','Yes'][x==l[0] and abs(y)==abs(l[1])])
else:
    print(['No','Yes'][cango(l[2::2],x-l[0]) and cango(l[1::2],y)])