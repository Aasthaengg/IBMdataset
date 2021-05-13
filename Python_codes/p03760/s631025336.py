O = input()
E = input()
ans = []

for n in range(len(E)):
  ans.append(O[n])
  ans.append(E[n])

if len(O) != len(E):
  ans.append(O[-1])
  
print("".join(ans))