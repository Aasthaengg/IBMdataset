N, K = map(int, input().split())
A = list(map(int, input().split()))

"""
dp[i]: 残りの石の個数がiの局面で手番が回ってきたときに勝つか負けるか。(boolean)
"""
dp = [False] * (K + 1)

for i in range(K+1):
    for a in A:
        if i - a >= 0:
            if not dp[i - a]:
                dp[i] = True
                continue
if dp[K]:
    print("First")
else:
    print("Second")
