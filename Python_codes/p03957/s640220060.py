S = input()

c = []
f = []

for i, si in enumerate(S):
    if si == 'C':
        c.append(i)
    elif si == 'F':
        f.append(i)

if len(c) == 0 or len(f) == 0:
    print('No')
elif min(c) < max(f):
    print('Yes')
else:
    print('No')