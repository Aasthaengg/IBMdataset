n,c = map(int,input().split())
L = [[] for i in range(c)]
for i in range(n):
    s,t,k = map(int,input().split())
    L[k-1].append([s,t])
for i in range(c):
    L[i].sort()
for i in range(c):
    d = [0]*(10**5+1)
    T = []
    for j in range(len(L[i])):
        d[L[i][j][0]] += 1
        d[L[i][j][1]] -= 1
    for j in range(10**5):
        d[j+1] += d[j]
    cur = 0
    start = 0
    end = 0
    for j in range(10**5+1):
        if d[j] == 1 and cur == 0:
            start = j
            cur = 1
        elif d[j] == 0 and cur == 1:
            end = j
            cur = 0
            T.append([start*2-1, end*2])
    L[i] = T
dp = [0]*(10**5)*3
ans = 0
for i in range(c):
    for j in range(len(L[i])):
        dp[L[i][j][0]] += 1
        dp[L[i][j][1]] -= 1
for j in range(1,(10**5)*2+3):
    dp[j] = dp[j-1]+dp[j]
    ans = max(ans, dp[j])
print(ans)
