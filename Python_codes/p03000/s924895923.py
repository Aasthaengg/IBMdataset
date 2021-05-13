n, x = map(int, input().split())
L = list(map(int, input().split()))
dist = 0
res = 1
for l in L:
    dist += l
    if dist <= x:
        res += 1
print(res)
