n, t = map(int, input().split())
a = list(map(int, input().split()))

ma = a[-1]
m = 1
maxsaeki = 0
ans = 0

for i in range(n-2,-1,-1):
    if a[i] > ma:
        ma = a[i]
        m = 1
    elif a[i] < ma:
        if (ma - a[i]) > maxsaeki:
            maxsaeki = ma-a[i]
            ans = 1
        elif (ma - a[i]) == maxsaeki:
            ans += 1

print(ans)