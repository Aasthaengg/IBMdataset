s = input().rstrip()
t = input().rstrip()

m = dict()

for a, b in zip(s, t):
    if a in m and b != m[a]:
        print('No')
        exit()

    m[a] = b

if len(m) == len(set(m.values())):
    print('Yes')
else:
    print('No')
