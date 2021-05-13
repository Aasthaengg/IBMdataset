from math import sqrt
s = input().split()
t = sqrt(int(''.join(s)))
print('Yes' if t.is_integer() else 'No')