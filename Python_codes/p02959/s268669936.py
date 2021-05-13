n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

for i in range(n):
    if a[i] >= b[i]:
        ans += b[i]
    else:
        val = b[i] - a[i]
        if a[i+1] - val <= 0:
            ans += a[i] + a[i+1]
            a[i+1] = 0
        else:
            ans += b[i]
            a[i+1] = a[i+1] - val

print(ans)