S = input()
s = list(S)
n = len(s)
ans = [[0 for i in range(13)]for i in range(n)]
mod = 10**9+7
if s[0] == '?':
    for i in range(10):
        ans[0][i] += 1
else:
    ans[0][int(s[0])] += 1
for i in range(n-1):
    if s[i+1] == '?':
        for j in range(10):
            for k in range(13):
                ans[i+1][(10*k+j)%13] += ans[i][k]%mod
    else:
        for k in range(13):
            ans[i+1][(10*k+int(s[i+1]))%13] += ans[i][k]%mod
print((ans[n-1][5])%(10**9+7))