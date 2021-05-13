alp = 'abcdefghijklmnopqrstuvwxyz'

d = {c:False for c in alp}

s = open(0).read().rstrip()

for c in list(s):
    d[c] = True

isnone = True
for c,b in d.items():
    if not b:
        isnone = False
        print(c)
        break
if isnone:
    print('None')