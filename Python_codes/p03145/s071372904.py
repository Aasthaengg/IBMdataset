line = input()
sides= [int(n) for n in line.split()]
sides.sort()
area = round(sides[0] * sides[1]/2)
print(area)