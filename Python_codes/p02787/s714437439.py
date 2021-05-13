def ceil(x,p):
    if x%p==0:
        return x//p
    else:
        return x//p+1

def main():
    INF = 10**9
    h,n = map(int,input().split())
    spell = []
    for _ in range(n):
        spell.append(tuple(map(int,input().split())))

    dp = [[INF]*(h+1) for _ in range(n+1)]

    for i,item in enumerate(spell):
        a,b = item
        for j in range(h):
            if j-a<0:
                dp[i+1][j+1] = min(dp[i][j+1],b*ceil(j+1,a))
            else:
                dp[i+1][j+1] = min(dp[i][j+1],dp[i+1][j+1-a]+b)
        
    print(dp[n][h])
main()