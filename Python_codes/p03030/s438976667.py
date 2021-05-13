n = int(input())
res = []
for i in range(1, n+1):
    s, p = input().split()
    res.append((s, -int(p), i))

res.sort()
for _, _, i in res:
    print(i)
