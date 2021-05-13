N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [0 for i in range(K+1)]
# dp[K] := 残りKこで初めて、先手が勝つような場合 1 ,後手 が勝つような場合 0
for i in range(1, K+1):
    is_first_win = False
    for v in a:
        if i-v >= 0 and dp[i-v] == 0:
            is_first_win = True
            break
    if is_first_win:
        dp[i] = 1
if dp[K]:
    print("First")
else:
    print("Second")
