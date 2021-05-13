S = input()
T = input()

t2s = {}
s2t = {}

for s, t in zip(S, T):
    if s2t.get(s, t) != t:
        print('No')
        break
    if t2s.get(t, s) != s:
        print('No')
        break
    s2t[s] = t
    t2s[t] = s
else:
    print('Yes')
