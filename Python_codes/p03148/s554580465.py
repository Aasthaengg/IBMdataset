n, nTake = map(int, input().split())
a = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: -x[1])

totalTaste = 0
same = []
types = set()
for i in range(nTake):
    type, taste = a[i]
    totalTaste += taste
    if type not in types:
        types.add(type)
    else:
        same.append(taste)

rem = []
typesRem = set()
for i in range(nTake, n):
    type, taste = a[i]
    if type not in types and type not in typesRem:
        typesRem.add(type)
        rem.append(taste)

same.sort()
rem.sort(key=lambda x: -x)
ret = totalTaste + len(types) ** 2
curTotal = totalTaste
for i in range(min(len(same), len(rem))):
    curTotal = curTotal - same[i] + rem[i]
    ret = max(ret, curTotal + (len(types) + i + 1) ** 2)
print(ret)