a,b = [int(n) for n in input().split()]

c = (b - 1)/(a - 1)
add = 1 - (c == int(c))
c = int(c) + add

print(c)
