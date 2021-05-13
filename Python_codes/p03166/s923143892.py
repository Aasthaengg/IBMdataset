import sys
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())

xy = [[] for i in range(n)]

for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    xy[x].append(y)
    #xy[y].append(x)
    
#xy = [[int(i)-1 for i in input().split()] for j in range(m)]
chk = [0]*n
dp = [0]*n

#print(xy)

def f(x):
    #global dp,chk
    if chk[x] == 1:
        return dp[x]
    fans = 0
    chk[x] = 1
    for i in range(len(xy[x])):
        fans = max(fans,f(xy[x][i])+1)
    dp[x] = fans
    #print(dp,chk)
    return dp[x]

ans = 0

for i in range(n):
    ans = max(ans,f(i))
    #print(f(i))
    
#print(dp)
print(ans)