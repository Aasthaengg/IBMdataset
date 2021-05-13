n = int(input())
a = list(map(int, input().split()))

ans = 1000
for i in range(n-1):
    if a[i] < a[i+1]:
        ans += (a[i+1] - a[i]) * (ans // a[i])

print(ans)
