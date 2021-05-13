n, m, q = map(int, input().split())
l = []
for i in range(q):
    l.append(list(map(int,input().split())))

t = [1]*(n+1)
ans = 0
while t[0] == 1:
    s = 0
    for i in range(q):
        if t[l[i][1]]-t[l[i][0]] == l[i][2]:
            s += l[i][3]
    ans = max(ans, s)
    k = n
    while t[k] == m and k >= 1:
        k -= 1
    t[k] += 1
    for i in range(k+1, n+1):
        t[i] = t[i-1]

print(ans)