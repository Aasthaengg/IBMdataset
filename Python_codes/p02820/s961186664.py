n, k = map(int,input().split())
r,s,p = map(int,input().split())
t = list(input())
dp = [0] * n #勝ったら1
ans = 0
for i in range(k):
    if t[i] == 'r':
        ans += p 
    elif t[i] == 's':
        ans += r 
    else:
        ans += s 
    dp[i] = 1
for i in range(k, n):
    if t[i] == 'r':
        if t[i - k] == t[i] and dp[i - k] == 1:
            continue
        else:
            dp[i] = 1
            ans += p 
            
    elif t[i] == 's':
        if t[i - k] == t[i] and dp[i - k] == 1:
            continue
        else:
            dp[i] = 1 
            ans += r 
    else:
        if t[i - k] == t[i] and dp[i - k] == 1:
            continue
        else:
            dp[i] = 1
            ans += s 

print(ans)
        
