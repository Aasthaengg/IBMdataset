n = int(input())
a = []
ans = 0
for i in range(n):
    a.append(sorted(input()))
a.sort()
flg = 0
for i in range(1,n):
    if a[flg] != a[i]:
        z = i - 1 - flg
        ans += (1 + z) * z // 2
        flg = i
z = n - 1 - flg
ans += (1 + z) * z // 2
print(ans)