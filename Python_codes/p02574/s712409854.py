n = int(input())
a = list(map(int,input().split()))
a.sort()
dp = [0 for i in range(a[-1])]
p = [0 for i in range(a[-1])]
for i in range(n):
    p[a[i]-1] += 1
ans = 1
for i in range(2,a[-1]+1):
    if dp[i-1] == 1:
        continue
    u = 0
    k = 1
    while i*k <= a[-1]:
        dp[i*k-1] = 1
        if p[i*k-1] != 0:
            u += p[i*k-1]
        k += 1
    if u == n:
        ans = -1
    elif u > 1:
        ans = min(ans,0)
if ans == 1:
    print('pairwise coprime')
elif ans == 0:
    print('setwise coprime')
elif a[0] == 1:
    print('setwise coprime')
else:
    print('not coprime')