S = input()
T = input()
stot = dict()
sset = set()
tset = set()
for s, t in zip(S, T):
    if s in sset:
        dt = stot[s]
        if t != dt:
            print('No')
            break
    else:
        if not t in tset:
            stot[s] = t
            sset.add(s)
            tset.add(t)
        else:
            print('No')
            break
else:
    print('Yes')
