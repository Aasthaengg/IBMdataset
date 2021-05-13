ab = list(map(int, input().split(' ')))
a = ab[0]
b = ab[1]
if b % a == 0:
    print(a + b)
else:
    print(b - a)