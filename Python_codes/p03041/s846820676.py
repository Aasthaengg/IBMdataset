x,y = [int(x) for x in input().split()]
z = input()
print(z[:y-1]+z[y-1].lower() + z[y:])
