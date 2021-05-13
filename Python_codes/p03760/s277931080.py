O = input()
E = input()
Ol = len(O)
El = len(E)
alllen = Ol + El
num = 0
num_2 = 0
pw = ""
for i in range(alllen):
  if i % 2 == 0:
    pw+=O[num]
    num+=1
  else:
    pw+=E[num_2]
    num_2+=1
print(pw)
