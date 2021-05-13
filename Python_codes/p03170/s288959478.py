n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

dp = [False]*(k+1)


for i,x in enumerate(dp):
    if not x:        
        for ai in a:
            if i+ai <= k:dp[i+ai] = True
    

if dp[k]:print('First')
else : print('Second')