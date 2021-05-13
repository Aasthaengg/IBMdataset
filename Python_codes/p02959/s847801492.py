n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i+1] + a[i] > b[i]:
        ans += b[i]
        a[i+1] = min(a[i+1], a[i] + a[i+1] - b[i])
    else:
        ans += a[i] + a[i+1]
        a[i+1] = 0
print(ans)
