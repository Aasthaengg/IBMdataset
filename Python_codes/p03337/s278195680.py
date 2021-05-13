line = input()
a, b = [int(n) for n in line.split()]

s = a + b
sub = a - b
m = a * b

if s>=sub and s>=m:
    print(s)
elif sub>=s and sub>=m:
    print(sub)
else:
    print(m)