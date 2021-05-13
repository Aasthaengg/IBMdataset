from copy import copy
n = int(input())
p = list(map(int, input().split()))
q = sorted(p)
ret = 'NO'
for i in range(n-1):
    for j in range(i, n):
        r = copy(p)
        r[i] = p[j]
        r[j] = p[i]
        if q == r:
            ret = 'YES'
            break
print(ret)