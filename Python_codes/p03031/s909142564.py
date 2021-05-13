n, m = map(int, input().split())
ks = [list(map(int, input().split())) for i in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(2**n):
    l = [False] * n
    for j in range(n):
        if (i>>j) & 1:
            l[j] = True
    for j in range(m):
        if [l[k-1] for k in ks[j][1:]].count(True) % 2 != p[j]:
            break
    else:
        ans += 1
print(ans)