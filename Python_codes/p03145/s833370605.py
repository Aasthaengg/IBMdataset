line = input()
v = [int(n) for n in line.split()]
c1 = min(v[0], v[1], v[2])
v.remove(c1)
c2 = min(v[0], v[1])
print(int((c1*c2)/2))