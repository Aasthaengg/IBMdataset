import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,K,*A = map(int,read().split())

dp = [0]*(K+1) # bitset
for n in range(K):
    if not dp[n]:
        for a in A:
            if n+a>K:
                break
            dp[n+a]=1

answer = 'First' if dp[-1] else 'Second'
print(answer)