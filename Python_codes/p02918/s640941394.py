n, k = map(int, input().split())
s = list(input())
v = s[0]
cnt = 0
a = []
for t in s:
    if t == v:
        cnt += 1
    else:
        a.append(cnt)
        cnt = 1
        v = t
a.append(cnt)
la = len(a)
b, c = [0] * (la + 1), [0] * (la + 1)
for i in range(1, la + 1):
    b[i] = b[i - 1] + a[i - 1]
    c[i] = b[i] - i
l = 2 * k + 1
if la < l:
    print(n - 1)
    exit()
ans = 0
i, j = l, 0
while True:
    ans = max(ans, b[i] - b[j] + c[la] + c[j] - c[i] - 1)
    i += 1
    j += 1
    if i > la:
        print(ans)
        exit()