import itertools
n = int(input())
l = []
for i in range(n):
    d = int(input())
    for dd in range(d):
        x, y = map(int, input().split())
        l.append([i, x-1, y])
 
ans = 0
for p in itertools.product([0, 1], repeat=n):
    for ll in l:
        if p[ll[0]] == 1 and p[ll[1]] != ll[2]:
            break
    else:
        ans = max(ans, sum(p))
print(ans)