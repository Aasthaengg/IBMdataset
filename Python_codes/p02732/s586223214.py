n = int(input())
a = list(map(int, input().split()))
d = {}

for ai in a:
    if ai in d:
        d[ai] += 1
    else:
        d[ai] = 1

cnt = sum([value*(value-1)//2 for value in d.values()])

for i in range(n):
    val = d[a[i]]
    res = cnt - val*(val-1)//2

    if val >= 3:
        res += (val-1)*(val-2)//2

    print(res)