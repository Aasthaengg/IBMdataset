O = input()
E = input()

x = []
for i in range(len(E)):
    x.append(O[i])
    x.append(E[i])
if len(O)!=len(E):
    x.append(O[-1])
s = ''.join(x)
print(s)
