O = input()
E = input()

for o, e in zip(O, E):
    print(o + e, end="")

if len(O) == len(E):
    print()
else:
    print(O[-1])