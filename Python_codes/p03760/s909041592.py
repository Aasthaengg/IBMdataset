O = input()
E = input()

OE = O + E
ans = ""
for i in range(len(OE)):
  if i%2==0:
    ans = ans + O[i//2]
  else:
    ans = ans + E[i//2]

print(ans)
