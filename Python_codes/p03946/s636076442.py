n, t = map(int, input().split())
ls = list(map(int, input().split()))
ms = []
m = ls[-1]
for x in ls[1:][::-1]:
    m = max(m, x)
    ms.append(m)
ms = ms[::-1]
ds = [m - x for x, m in zip(ls[:-1], ms)]
m = max(ds)
print(sum([1 for d in ds if d == m]))