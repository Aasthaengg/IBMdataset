import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,K = map(int,input().split())
A = [int(i) for i in input().split()]

# dp[i]: 石の個数が残りi個の局面での勝敗
dp = [False] * (K+1)

# 初期条件
dp[0] = False

for i in range(K+1):
    for a in A:
        if i+a > K:
            continue
        dp[i+a] |= not dp[i]

if dp[-1]:
    print("First")
else:
    print("Second")