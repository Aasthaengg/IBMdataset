from itertools import product
s = input().strip()
for x in product(("+","-"),repeat=3):
    y = s[0]+x[0]+s[1]+x[1]+s[2]+x[2]+s[3]
    if eval(y)==7:
        break
print(y+"=7")