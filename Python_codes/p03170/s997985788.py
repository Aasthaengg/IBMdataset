import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,K = map(int,input().split())
A = [int(x) for x in input().split()]

dp = [False] * (K+K+1)
for i in range(K):
    if not dp[i]:
        for a in A:
            dp[i+a] = True

answer = 'First' if dp[K] else 'Second'
print(answer)