n = int(input())
a = list(map(int, input().split()))
a.sort()
aMax = a[-1]
ans = 0
dp = [1] * (aMax+1)

for i in range(n-1):
    p = a[i]
    if dp[p] == 1:
        for j in range(aMax//p+1):
            dp[p*j] = 0
        if a[i] != a[i+1]:
            ans += 1
if dp[aMax] == 1:
    ans += 1
print(ans)