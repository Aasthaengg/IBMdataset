O = input()
E = input()

l = min(len(O), len(E))
s = ""
for i in range(l):
  s = s + O[i] + E[i]

if len(O) > len(E):
  s = s + O[len(O)-1]

print(s)
