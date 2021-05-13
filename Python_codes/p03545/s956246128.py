ABCD = input()

for i in range(2**3):
  f = ABCD[0]
  for j in range(3):
       if ((i >> j) & 1):
        f += "-"
       else:
        f += "+"
       f += ABCD[j+1]

  if eval(f) == 7:
    print(f+"=7")
    exit()