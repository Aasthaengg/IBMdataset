n, m = map(int, input().split())
kk = []
ss = []
for i in range(m):
    ks = list(map(int, input().split()))
    k = ks[0]
    s = ks[1:]
    kk.append(k)
    ss.append(s)
p = list(map(int, input().split()))
ans = 0

for i in range(2 ** (n)):
    check = [0 for i in range(m)]
    for j in range(n):
        if i >> j & 1:
            for l in range(m):
                if (j + 1) in ss[l]:
                    check[l] = (check[l] + 1) % 2
    if check == p:
        ans += 1
print(ans)
