import sys
input = sys.stdin.readline

N = int(input())
C = [int(input()) for _ in range(N)]+[-1]
l = []

for i in range(N):
    if C[i]!=C[i+1]:
        l.append(C[i])

if len(l)==1:
    print(1)
    exit()
    
dp = [0]*(len(l))
acc = [0]*(2*10**5+100)
dp[0] = 1
acc[l[0]] = 1
acc[l[1]] = 1
MOD = 10**9+7

for i in range(1, len(l)):
    dp[i] = acc[l[i]]
    
    if i<len(l)-1:
        acc[l[i+1]] += dp[i]
        acc[l[i+1]] %= MOD

print(dp[-1])