O = input()
E = input()
if len(O) == len(E):
    print("".join(o + e for o, e in zip(O, E)))
else:
    print("".join(o + e for o, e in zip(O[:-1], E)) + O[-1])