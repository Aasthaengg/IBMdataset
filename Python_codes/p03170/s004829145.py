N, K = map(int, input().split())
A = [int(i) for i in input().split()]

dp = [0 for _ in range(K+100)]

for i in range(K+1):
    flg = False
    for a in A:
        if i-a >= 0 and dp[i-a] == -1:
            flg = True
    if flg:
        dp[i] = 1
    else:
        dp[i] = -1

if dp[K] == 1:
    print('First')
else:
    print('Second')
