q = input()
x, y = q.split()
x, y = int(x), int(y)
if (x * y) % 2 == 0:
    print("Even")
else:
    print("Odd")
