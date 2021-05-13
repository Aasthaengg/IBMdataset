import sys
input = sys.stdin.readline

N,K=map(int,input().split())
a = list(map(int, input().split()))
dp = [False]*(K+1)

for i in range(1,K+1):
    for j in range(N):
        if i-a[j]<0: break
        if not(dp[i-a[j]]):
            dp[i]=True
            break
if dp[K]:
    print("First")
else:
    print("Second")