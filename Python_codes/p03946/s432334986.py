from collections import defaultdict
# d = defaultdict(int)で0で初期化
# d = defaultdict(lambda: 100)で100で初期化
n, t = map(int, input().split())
a = list(map(int, input().split()))
mn = 1 << 32
i = 0
d = defaultdict(int)
while i < n - 1:
    if a[i] < mn:
        eqmn = 1
        mn = a[i]
        while i < n - 1 and a[i] == a[i + 1]:
            eqmn += 1
            i += 1

    elif a[i] < a[i + 1]:
        eqmx = 1
        while i < n - 1 and a[i] <= a[i + 1]:
            if a[i] == a[i + 1]:
                eqmx += 1
            else:
                eqmx = 1
            i += 1
        mx = a[i]
        d[mx - mn] += min(eqmx, eqmn)

    else:
        i += 1

print(d[max(d.keys())])
