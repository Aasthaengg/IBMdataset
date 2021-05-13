N,K = map(int,input().split())

POINT = tuple(map(int,input().split()))

T = input()
m = {'r':0,'s':1,'p':2}
T = [m[h] for h in T]

def helper(T):
    dp = [0]*3
    for t in T:
        wh = (t-1)%3
        op = max(dp)
        dp[wh] = max(v for i,v in enumerate(dp) if i != wh)+POINT[wh]
        for h in range(3):
            if h != wh:
                dp[h] = op
    return max(dp)


res = sum(helper(T[i::K]) for i in range(min(K,N)))

print(res)

