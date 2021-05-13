from sys import stdin

data = stdin.readlines()

a = int(data[0].split()[0])

b = int(data[0].split()[1])

x = a * b

if x % 2 == 0:
    print("Even")
else:
    print("Odd")