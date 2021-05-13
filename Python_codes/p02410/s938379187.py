n, m = map(int, raw_input().split())

a = []
for i in range(n):
    a.append(map(int, raw_input().split()))
b = []
for j in range(m):
    b.append(int(raw_input()))

ans = []
for i in range(n):
    tmp = 0
    for j in range(m):
        tmp += a[i][j] * b[j]
    ans.append(tmp)

print "\n".join(map(str, ans))