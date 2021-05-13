n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 10**18
for i in range(n-1):
    if abs(a[i] - a[-1]/2) < abs(ans - a[-1]/2):
        ans = a[i]
print(a[-1],ans)