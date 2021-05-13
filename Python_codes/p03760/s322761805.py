o = input()
e = input()
k = []

for i in range(len(e)):
    k.append(o[i])
    k.append(e[i])

if len(o) > len(e):
    k.append(o[-1])

print(''.join(k))