x,y,z = [int(a) for a in input().split()]

print(min(min(x+y,y+z),x+z))
