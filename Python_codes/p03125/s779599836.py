source = input().split()
a, b = int(source[0]), int(source[1])
if b % a == 0:
    print(a + b)
else:
    print(b - a)