import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,K,*A = map(int,read().split())

dp = [0]*(K+K+1)
for n in range(K):
    if not dp[n]:
        for a in A:
            dp[n+a]=1

answer = 'First' if dp[K] else 'Second'
print(answer)
