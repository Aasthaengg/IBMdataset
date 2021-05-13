O = input()
E = input()

L = []
for i in range(len(O)):
  L.append(O[i])
  L.append("")

for j in range(len(E)):
  L[2*j+1] = E[j]

l = ""
for i in range(len(L)):
  l = l + L[i]

print(l)