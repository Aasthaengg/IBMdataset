input_str = input()

a, b, c = input_str.split()
a = int(a)
b = int(b)
c = int(c)

if a + b >= c:
    print(b + c)
else:
    print((a+b)*2 +1 - a)