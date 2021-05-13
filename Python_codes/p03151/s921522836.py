n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = []
ans = 0
m = 0
if sum(a) < sum(b):
    print(-1)
    exit()
for i in range(n):
    if a[i] < b[i]:
        ans += 1
        m += b[i] - a[i]
    else:
        l.append(a[i] - b[i])
l = list(reversed(sorted(l)))
for i in l:
    if m > 0:
        m -= i
        ans += 1
print(ans)
