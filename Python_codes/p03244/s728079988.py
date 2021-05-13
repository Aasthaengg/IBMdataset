from collections import Counter
n = int(input())
v = list(map(int, input().split()))
e = v[::2]
o = v[1::2]
ce = sorted([(v, k) for k, v in Counter(e).items()], reverse=True)
co = sorted([(v, k) for k, v in Counter(o).items()], reverse=True)
if ce[0][1] == co[0][1]:
    if len(ce) == 1 and len(co) == 1:
        print(len(o))
    elif len(ce) == 1:
        print(len(o) + len(e) - ce[0][0] - co[1][0])
    elif len(co) == 1:
        print(len(o) + len(e) - ce[1][0] - co[0][0])
    else:
        print(len(e) + len(o) - max(ce[1][0] + co[0][0], ce[0][0] + co[1][0]))
else:
    print(len(e) + len(o) - ce[0][0] - co[0][0])
