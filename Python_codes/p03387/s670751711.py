a, b, c = map(int, input().split())

if a >= b and a >= c:
    if (2*a - b - c) % 2 == 0:
        print(int((2*a - b - c)/2))
    else:
        print(int((2*a - b - c)//2 + 2))
elif b >= a and b >= c:
    if (2*b -a -c) %2 == 0:
        print(int((2*b -a -c)/2))
    else:
        print(int((2*b -a -c)//2 +2))
else:
    if (2*c -b-a) % 2 ==0:
        print(int((2*c -b-a)/2))
    else:
        print(int((2*c -b-a)//2 +2))
