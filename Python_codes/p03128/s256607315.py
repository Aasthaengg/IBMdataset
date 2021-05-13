N, M = map(int, input().split())
A = list(map(int, input().split()))

def nax(a, b):
    if a == '-':
        return b
    if len(a) != len(b):
        return a if len(a)>len(b) else b
    return a if a>b else b


match = [2,5,5,4,5,6,3,7,6]
# dp[i]  : iほんのマッチを使ってできる数値の最大値
dp = ['-'] * 11000
dp[0] = ''

for i in range(N+1):
    if dp[i] == '-':
        continue
    for a in A:
        dp[i+match[a-1]] = nax(dp[i+match[a-1]], dp[i] + chr(ord('0') + a))

print(dp[N])