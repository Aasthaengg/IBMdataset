a,b,c,d,e,f=map(int,input().split())
dp=[0]*(3000+1)
for i in range(f//c+1):
    for j in range(f//d+1):
        if c*i+d*j<=3000:
            dp[c*i+d*j]=c*i+d*j
for i in range(1,3001):
    dp[i]=max(dp[i],dp[i-1])
ans_den=min(100*a,100*b)
ans_num=0
ans=0
for i in range(f//a+1):
    for j in range(f//b+1):
        #so we have put 100*a*i +100*b*j amount of water 
        w=100*i*a+100*j*b
        if w>f or w==0:
            continue
        rem=f-w
        sugar_max=min(e*(i*a+j*b),rem)
        val=dp[sugar_max]
        if val/(w+val)>ans:
            ans=val/(w+val)
            ans_num=val
            ans_den=w+val
print(ans_den,ans_num)

