line = input()
a, b = [int(n) for n in line.split()]

largest = 0

x = [a+b, a-b, a*b]
x.sort()

print(x[-1])

