z = input()

a,b = z.split()
c = int(a)
d = int(b)

if c < d:
    print('a < b')
elif c > d:
    print('a > b')
else:
    print('a == b')