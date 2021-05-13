a, b, c = [int(i) for i in input().split()]

if b > a*c:
    print(c)
else:
    print(b//a)