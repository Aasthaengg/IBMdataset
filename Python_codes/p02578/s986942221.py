n = int(input())
a = list(map(int, input().split(" ")))
ans = 0
for i in range(n):
    if i != 0:
        if a[i] < a[i-1]:
            ans += a[i-1]
            ans -= a[i]
            a[i] = a[i-1]

print(ans)