
from collections import defaultdict

S = input()
T = input()

ctr_s = defaultdict(list)
ctr_t = defaultdict(list)
for i in range(len(S)):
    ctr_s[S[i]].append(i)
    ctr_t[T[i]].append(i)

ok = True
for key in ctr_s:
    char = T[ctr_s[key][0]]
    ok &= len(ctr_s[key]) == len(ctr_t[char])
    ok &= all(u == v for u, v in zip(ctr_s[key], ctr_t[char]))

if ok:
    print("Yes")
else:
    print("No")
