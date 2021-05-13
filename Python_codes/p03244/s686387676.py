n = int(input())
v = list(map(int, input().split()))

from collections import Counter, defaultdict
e, o = Counter(), Counter()
for i in range(n):
    if i % 2 == 0:
        e[v[i]] += 1
    else:
        o[v[i]] += 1

e_inv = defaultdict(list)
for key in e:
    e_inv[n // 2 - e[key]].append(key)
e_inv[n // 2].append(0)

o_inv = defaultdict(list)
for key in o:
    o_inv[n // 2 - o[key]].append(key)
o_inv[n // 2].append(0)

e_inv_keys = sorted(list(e_inv.keys()))
o_inv_keys = sorted(list(o_inv.keys()))

l1, l2 = e_inv[e_inv_keys[0]], o_inv[o_inv_keys[0]]
if len(l1) == 1 and len(l2) == 1 and l1 == l2:
    ans = min(e_inv_keys[0] + o_inv_keys[1], e_inv_keys[1] + o_inv_keys[0])
else:
    ans = e_inv_keys[0] + o_inv_keys[0]

print(ans)
