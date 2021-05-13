from math import ceil
x = int(input())
q, mod = divmod(x, 11)
print(q * 2 + ceil(mod / 6))