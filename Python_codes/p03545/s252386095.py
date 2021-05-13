from itertools import product

a,b,c,d=map(int,list(input()))
op = ['+','-']
for p in product(range(2),repeat=3):
  txt=f'{a}{op[p[0]]}{b}{op[p[1]]}{c}{op[p[2]]}{d}'
  if eval(txt)==7:
    print(txt+'=7')
    exit()