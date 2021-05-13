n=int(input())
c=[int(input()) for _ in range(n)]
x=[c[0]]
for i in range(1,n):
    if c[i]!=c[i-1]:
        x.append(c[i])
#print(x)

dp=[0 for _ in range(n)]
res=[[] for _ in range(max(x)+1)]
res[x[0]].append(0)
res2=[0 for _ in range(max(x)+1)]
for i in range(1,len(x)):
    if len(res[x[i]])>0:
        if res[x[i]][-1]==0:#左端スタートで１つ目の場合
            dp[i]=dp[i-1]+1
        else:
            dp[i]=dp[i-1]+len(res[x[i]])+res2[x[i]]
            #print(res2[x[i]])
    else:
        dp[i]=dp[i-1]
    res[x[i]].append(i)
    res2[x[i]]+=dp[i-1]
    #print(dp,res2)
print((dp[len(x)-1]+1)%(10**9+7))
#print(res)