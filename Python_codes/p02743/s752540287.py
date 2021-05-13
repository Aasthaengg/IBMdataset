from math import sqrt
a, b, c = [int(w) for w in input().split()]
cond = 4*a*b < (c-a-b)**2 and (c-a-b) > 0


print("Yes" if cond else "No")
