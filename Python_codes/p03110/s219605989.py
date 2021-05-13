n = int(input())
keep = []
ans = 0
for i in range(n):
    s = list(input().split())
    keep.append(s)
for j in range(n):
    st = keep[j]
    if st[1] == 'JPY':
        ans += float(st[0])
    else:
        ans += float(st[0]) * 380000
print(ans)
