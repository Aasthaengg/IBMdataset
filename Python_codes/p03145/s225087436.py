x = input()
k=x.split(" ")

ab= int(k[0])
bc= int(k[1])
ca= int(k[2])

v = [ab,bc,ca]
v.remove(max(v))

print(int(v[0]*v[1]*0.5))
