from itertools import product

s=input()

for op in product(["+","-"],repeat=3):
  formula =""
  for i in range(3):
    formula+=s[i]+op[i]
  formula+=s[-1]
  if eval(formula)==7:
    print(formula+"=7")
    exit()