O = input()
E = input()
for o, e in zip(O, E):
    print(o, e, end='', sep='')
if len(O) != len(E):
    print(O[-1])