n = int(input())
a = []
for _ in range(n):
    c0, c1 = map(int, input().split())
    a.append([c0-c1, c0+c1])
a.sort(key=lambda x: x[1])
ans, b = 1, a[0][1]
for i in a[1:]:
    if b <= i[0]:
        b = i[1]
        ans += 1
print(ans)
