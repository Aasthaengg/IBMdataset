S = input()
T = input()
s = {d:[] for d in set(S)}
t = {d:[] for d in set(T)}

for i, (j,k) in enumerate(zip(S,T)):
    s[j] += [i]
    t[k] += [i]
a = sorted(s.values())
b = sorted(t.values())

print('Yes' if a==b else "No")