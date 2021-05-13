n,m = map(int, input().split())
l = [2,5,5,4,5,6,3,7,6]

a = list(map(int, input().split()))
a.sort(reverse=True)
key = set([l[i-1] for i in a])

dp = [-float("inf")]*(n+1)
dp[0] = 0
for i in range(n):
    for j in key:
        if i+j <= n:
            dp[i+j] = max(dp[i+j], dp[i]+1)

i = n
ans = []
while i > 0:
    for ai in a:
        if i-l[ai-1] >= 0 and dp[i]-dp[i-l[ai-1]] == 1:
            ans.append(ai)
            i -= l[ai-1]
            break
print("".join(map(str, ans)))