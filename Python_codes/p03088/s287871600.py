# maspyさんの見て書いた。
# 最初自分で書いたけど、改善していたらほぼ写経になってしまった。。。

from collections import defaultdict

n = int(input())
m = 10**9+7

dp = [defaultdict(int) for i in range(n+1)]
dp[0]['']=1

def check(s):
    if 'AGC' in s:
        return False
    for i in range(len(s)-1):
        l = list(s)
        l[i],l[i+1]=l[i+1],l[i]
        t = ''.join(l)
        if 'AGC' in t:
            return False
    return True

for i in range(n):
    for k,v in dp[i].items():
        for x in 'AGCT':
            y = k[-3:]+x
            if check(y):
                dp[i+1][y]+=v

print(sum(dp[n].values())%m)

