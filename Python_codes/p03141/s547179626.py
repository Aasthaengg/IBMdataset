n = int(input())
a = []
b = []
c = []
for i in range(n):
    line = list(map(int, input().split()))
    a.append(line[0])
    b.append(line[1])
    c.append([line[0] + line[1], i])
c.sort(key = lambda x:x[0], reverse = True)
ans = 0
for i in range(n):
    if i%2 == 0:
        ans += a[c[i][1]]
    else:
        ans -= b[c[i][1]]
print(ans)
