n, t = map(int, input().split())
a = list(map(int, input().split()))
m = float('inf')
l = []
max_s = 0
ans = 0
for i in range(n):
    m = min(m, a[i])
    max_s =max(a[i]-m, max_s)
    l.append(max(a[i] - m, 0))
for i in l:
    if i == max_s:
        ans += 1
# print(l)
print(ans)
