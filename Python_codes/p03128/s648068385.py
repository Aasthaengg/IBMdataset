N,M = map(int,input().split())
A = list(map(int,input().split()))
num = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}

def lenmax(a,b):
    if len(a) > len(b):
        return a
    elif len(a) < len(b):
        return b
    return max(a,b)

dp = ['-' for i in range(10**4+10)]
dp[0] = ''
for i in range(N+1):
    if dp[i] == '-':
        continue
    for a in A:
        dp[i+num[a]] = lenmax(dp[i+num[a]],dp[i]+str(a))
print(dp[N])