n = int(input())
a = list(map(int, input().split()))
tmp = a[0]
ans = 0
for i in a:
    diff = tmp - i
    if diff > 0:
        ans += diff
        tmp = i + diff
        continue
    tmp = i
print(ans)

