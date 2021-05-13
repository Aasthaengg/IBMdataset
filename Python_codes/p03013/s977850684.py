from collections import deque
def C():
    N, M = map(int, input().split())
    A = set([int(input()) for _ in range(M)])
    dp = deque([1, 1 if 1 not in A else 0])
    MOD = 1000000007
    for i in range(2,N+1):
        #print(i, dp)
        if i in A:
            dp.append(0)
        else:
            dp.append((dp[0]+dp[1]) % MOD)
        dp.popleft()
    print(dp[-1])

C()