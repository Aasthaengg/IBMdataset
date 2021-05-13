n = int(input())
a = list(map(int,input().split()))
ans = 0
place = [0]*n
active = sorted(a,reverse=True)
for i in range(n):
    place[i] = a.index(active[i])
    a[a.index(active[i])] = -1

#dp[x][y] x,y:0~n+1 (x[-1]=x[n+1]=0にすることで端の処理を楽にする)
dp = [[0 for i in range(n+2)]for j in range(n+2)]

for i in range(n):
    dp[0][i+1] = dp[0][i]+active[i]*abs(n-i-1-place[i])
    dp[i+1][0] = dp[i][0]+active[i]*abs(place[i]-i)



def check(mat):
    for i in range(len(mat)):
        print(mat[i])
    print("\n")


for i in range(n):
    for x in range(i+2):
        y = i+1 - x
        if x != 0 and y != 0:
            dp[x][y] = max(dp[x-1][y]+active[i]*abs(place[i]-x+1),dp[x][y-1]+active[i]*abs(n-y-place[i]))
            if i == n-1:
                ans = max(ans,dp[x][y])

print(ans)


