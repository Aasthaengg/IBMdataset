n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

aa = [0]
bb = [0]
for i in range(n):
    aa.append(aa[-1]+a[i])
for i in range(m):
    bb.append(bb[-1]+b[i])

d = 0
ans = 0
for i in range(n, -1, -1):
    c = k - aa[i]
    if c >= 0:
        for j in range(d, m+1):
            if bb[j] <= c:
                d = j
            else:
                break
        ans = max(ans, i+d)
print(ans)