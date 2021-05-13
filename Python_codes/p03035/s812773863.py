line = input()
a, b = [int(n) for n in line.split()]
if a>=13:
    print(b)
elif a>=6:
    b = b/2
    b = int(b)
    print(b)
else:
    print("0")