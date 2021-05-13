import math

a = int(input().replace(' ', ''))
b = math.sqrt(a)
r = 'Yes' if (b.is_integer()) else 'No'
print(r)