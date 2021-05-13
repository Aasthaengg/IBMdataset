O = input()
E = input()
a = ''

for o, e in zip(O, E):
    a += o + e
if len(O) != len(E):
    a += O[-1]
print(a)