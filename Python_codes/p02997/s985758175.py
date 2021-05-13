n,k = map(int,input().split())
mx = (n - 1) * (n - 2) // 2
if mx < k:
    print(-1)
    exit()

l,r = 1,2

res = []
for i in range(1, n):
    res.append([i, n])

while mx > k:
    mx -= 1
    res.append([l, r])
    if r == n - 1:
        l += 1
        r = l + 1
    else:
        r += 1

print(len(res))
for i in res:
    print(*i)