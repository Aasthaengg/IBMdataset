x = input()
a, b, c = tuple(x.split())
a = int(a)
b = int(b)
c = int(c)
abc = sorted([a, b, c])
print(abc[0], abc[1], abc[2])