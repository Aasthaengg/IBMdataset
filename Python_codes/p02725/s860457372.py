k, n = map(int,input().split())
a = list(map(int,input().split()))

ans = 10**6 + 1
for i in range(n):
    ans = min(ans, a[-1] - a[i])
    a.append(a[i]+k)
print(ans)
