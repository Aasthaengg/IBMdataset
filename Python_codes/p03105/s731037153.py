line = input()
a, b, c = [int(n) for n in line.split()]
b = b/a
b = int(b)
if b>c:
    print(c)
else:
    print(b)