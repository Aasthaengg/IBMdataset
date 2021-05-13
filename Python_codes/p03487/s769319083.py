N = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    d[i] = d[i] + 1 if i in d else 1
ans = 0
for i in d:
    if i < d[i]:
        ans += d[i]-i
    if i > d[i]:
        ans += d[i]
print(ans)

