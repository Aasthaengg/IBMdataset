O = input()
E = input()
l = min(len(O),len(E))
s = ""
for i in range(l):
  s = s+O[i]+E[i]
  
if s[2*(l-1)] == O[len(O)-1]:
  print(s)
else:
  print(s+O[len(O)-1])