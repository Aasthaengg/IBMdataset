s = int(input())
a = 10**9
if s == 10**18:
    print(0, 0, a, 0, 0, a)
else:
    x3 = a-(s%a)
    y3 = (s+x3)//a
    print(0, 0, a, 1, x3, y3)