from collections import Counter

h, w, m = map(int, input().split())
beds = [tuple(map(lambda x: int(x) - 1, input().split()))  for _ in range(m)]

bom_v = Counter(b[0] for b in beds)
bom_h = Counter(b[1] for b in beds)

v_max = max(bom_v.values())
h_max = max(bom_h.values())

cand = list(bom_v.values()).count(v_max) * list(bom_h.values()).count(h_max)
bombs = len([... for i, j in beds if bom_v[i] ==  v_max and bom_h[j] ==  h_max])

if cand - bombs > 0:
    print(v_max + h_max)
else:
    print(v_max + h_max - 1)