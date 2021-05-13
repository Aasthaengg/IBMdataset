ss = input()

S1 = []
S2 = []

a = 0
for ind, s in enumerate(ss):
    if '\\' == s:
        S1.append(ind)
    elif s == '/':
        if len(S1) == 0:
            continue
        i = S1.pop()
        a += ind - i
        t = 0
        while len(S2) > 0 and S2[-1][0] > i-1:
            v = S2.pop()
            t += v[1]
        S2.append((i, ind-i+t))

print(a)
if len(S2) == 0:
    print(0)
else:
    print(len(S2), ' '.join(map(lambda x: str(x[1]), S2)))