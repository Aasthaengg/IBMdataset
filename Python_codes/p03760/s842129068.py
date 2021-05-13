O = input()
E = input()

s = []
for i in range(len(E)):
  s.append(O[i])
  s.append(E[i])
if len(O) > len(E):
  s.append(O[-1])
  
print("".join(s))