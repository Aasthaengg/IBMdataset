n=input()[::-1]
n+="0"
lt=len(n)
dp=[[float('inf') for _ in range(2)] for j in range(lt+1)]
dp[0][0]=0

for i in range(0,lt):
    for j in range(2):
        x=int(n[i])
        x+=j #繰り上がり処理，あとに+11でもOK
        for num in range(0,10):
            ni = i + 1
            nj = 0
            b=num-x
            if b<0:
                b+=10
                nj=1
            dp[ni][nj]=min(dp[ni][nj],dp[i][j]+num+b)

print(dp[lt][0])