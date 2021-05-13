n = int(input())
dms = [tuple(input().split()) for _ in range(n)]

ans = 0
for dm in dms:
    if dm[1] == 'JPY':
        ans += float(dm[0])
    else:
        ans += float(dm[0]) * 380000
print(ans)
