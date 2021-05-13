S = input()
T = input()
stot = dict()
ttos = dict()
for s, t in zip(S, T):
    stot.setdefault(s, set())
    stot[s].add(t)
    ttos.setdefault(t, set())
    ttos[t].add(s)

ans = 'Yes'
for k, l in stot.items():
    if len(l) > 1:
        ans = 'No'
        break

for k, l in ttos.items():
    if len(l) > 1:
        ans = 'No'
        break
print(ans)
