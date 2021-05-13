from collections import Counter
n = int(input())
v = list(map(int, input().split()))
v1, v2 = [], []
for i in range(n):
    if i%2:
        v1.append(v[i])
    else:
        v2.append(v[i])
vv1 = Counter(v1).most_common()
vv2 = Counter(v2).most_common()
if vv1[0] != vv2[0]:
    print(n - vv1[0][1] - vv2[0][1])
else:
    if len(vv1) == len(vv2) == 1:
        print(n - max(vv1[0][1], vv2[0][1]))
    elif len(vv1) == 1 and len(vv2) == 2:
        print(n - vv1[0][1] - vv2[1][1])
    elif len(vv1) == 2 and len(vv2) == 1:
        print(n - vv1[1][1] - vv2[0][1])
    else:
        print(n - max(vv1[1][1] + vv2[0][1], vv1[0][1] + vv2[1][1]))