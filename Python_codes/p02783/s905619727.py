a,b = input().split()
c = int(a) // int(b)
if c * int(b) == int(a):
    print(c)
else:
    print(c + 1)


