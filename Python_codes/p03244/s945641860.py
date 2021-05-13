from collections import Counter
n = int(input())
v = list(map(int, input().split()))
o, e = v[0::2], v[1::2]
co, ce = Counter(o).most_common(), Counter(e).most_common()
if co[0][0] == ce[0][0]:
    if len(co) == len(ce) == 1:
        print(n // 2)
    elif len(co) == 1:
        print(n // 2 - ce[0][1])
    elif len(ce) == 1:
        print(n // 2 - co[0][1])
    else:
        print(min(n - (co[1][1] + ce[0][1]),n - (co[0][1] + ce[1][1])))
else:
    if len(co) == len(ce) == 1:
        print(0)
    elif len(co) == 1:
        print(n // 2 - ce[0][1])
    elif len(ce) == 1:
        print(n // 2 - co[0][1])
    else:
        print(n - (co[0][1] + ce[0][1]))