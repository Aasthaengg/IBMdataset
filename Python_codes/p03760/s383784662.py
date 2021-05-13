O = input()
E = input()
S = ""
for o, e in zip(O, E):
  S += o+e
print(S+O[-1] if len(O)-len(E) else S)