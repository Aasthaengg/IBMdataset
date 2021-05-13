n,m=map(int,input().split())
A=list(map(int,input().split()))
weight=[0,2,5,5,4,5,6,3,7,6]
dp=[-1]*(n+1)
dp[0]=0
for i in range(n+1):
    for a in A:
        if i+weight[a]<=n:
            dp[i+weight[a]]=max(dp[i+weight[a]],dp[i]*10+a)
print(dp[n])
'''
    dic={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
    a=sorted(list(map(int,input().split())),key=lambda x:(dic[x],-x))
    b=[0]*10
    i=0
    while(n!=0):
        b[a[i]]+=1
        n-=dic[a[i]]
        if n<dic[a[i]] and n!=0:
            while(n<dic[a[i+1]]):
                b[a[i]]-=1
                n+=dic[a[i]]
            i+=1
    print(a)
    print(b)
'''