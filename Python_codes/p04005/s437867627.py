a, b, c = map(int, input().split())

if (a % 2 == 0)|(b % 2 == 0)|(c % 2 == 0):
    print(0)
else:
    print(min(a*b, b*c, c*a))