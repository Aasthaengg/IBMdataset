n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [None]*(k+1)
ind = 0
while ind<a[0]:
    dp[ind] = False
    ind += 1
for i in range(ind, k+1):
    for j in a:
        if i-j<0:
            dp[i] = False
            break
        if not dp[i-j]:
            dp[i] = True
            break
    else:
        dp[i] = False
print('First' if dp[k] else 'Second')
