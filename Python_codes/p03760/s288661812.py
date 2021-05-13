O = input().strip()
E = input().strip()
p = ""
for x in zip(O, E):
    p += x[0]+x[1]
if len(O) != len(E):
    p += O[-1]
print(p)
