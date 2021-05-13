n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = str(input())
dp = [0]*n
fl = [True]*k
for i in range(n):
    if t[i] == "r":
        h = p
    elif  t[i] == "s":
        h = r
    else:
        h = s
    if i < k:
        if i == 0:
            dp[i] = h
            fl[i%k-1] = False
        else:
            dp[i] = h + dp[i-1]
            fl[i%k-1] = False
    else:
        if t[i] == t[i-k]:
            if fl[i%k-1] == True:
                dp[i] = dp[i-1]+h
                fl[i%k-1] = False
            else:
                dp[i] = dp[i-1]
                fl[i%k-1] = True
        else:
            dp[i] = dp[i-1] + h
            fl[i%k-1] = False    
print(dp[-1])