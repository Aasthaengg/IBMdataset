a = []
for i in range(5):
    a.append(int(input()))
p = 10
for i in range(5):
    if a[i] % 10 != 0:
        p = min(p,a[i]%10)
ans = 0
for i in range(5):
    if a[i] % 10 != 0:
        if a[i] % 10 == p:
            ans += a[i]
            p = 10
        else:
            ans += a[i] - a[i] % 10 + 10
    else:
        ans += a[i]
print(ans)