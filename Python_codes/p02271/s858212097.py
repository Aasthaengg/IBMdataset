n = int(input())
A = tuple(map(int,input().split()))
q = int(input())
Q = tuple(map(int, input().split()))
dp = [0]*(2**n)

for i in range(n):
    for j in range(1<<i):
        dp[j+(1<<i)] = dp[j] + A[i]

s = set(dp)
for n in Q:
    print("yes" if set([n]) & s else "no")