ins = input()
a,b,c = ins.split()

a, b = b, a
a, c = c, a

print(a,b,c)