o = input()
e = input()
n = []
e += ' '
for i in range(len(o)):
  n.append(o[i])
  n.append(e[i])
print(''.join(n).strip())
