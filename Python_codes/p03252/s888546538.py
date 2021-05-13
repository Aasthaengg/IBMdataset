from collections import defaultdict

s = input()
t = input()

in_deg = defaultdict(set)
out_deg = defaultdict(set)

for es, et in zip(s, t):
    out_deg[es].add(et)
    in_deg[et].add(es)

in_deg_mx = max(map(len, in_deg.values()))
out_deg_mx = max(map(len, out_deg.values()))

if in_deg_mx <= 1 and out_deg_mx <= 1:
    ans = "Yes"
else:
    ans = "No"

print(ans)
