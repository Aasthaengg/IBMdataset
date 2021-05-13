WIN  = 1
LOSE = 0

N, K = map(int, input().split())
a = [int(i) for i in input().split()]

Sa = set(a)
Sk = set()

dp = [LOSE] * (K+1)

for k in range(1, K+1):
    if k in Sa: 
        dp[k] = WIN
        Sk.add(k)
    else:
        for i in range(N):
            if k-a[i] >0:
                if k-a[i] not in Sk:
                    dp[k] = WIN
                    Sk.add(k)
                    break

#print(Sa, K, Sk)
#print(dp[1:])
if dp[-1] == 1:
    print('First')
else:
    print('Second')
