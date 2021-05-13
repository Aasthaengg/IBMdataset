ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))
n,m=mi()
c = li()
dp=list(range(n+1))
for i in c:
    if(i==1):
        continue
    for j in range(i,n+1):
        dp[j] = min(dp[j], dp[j-i]+1)
print(dp[n])
