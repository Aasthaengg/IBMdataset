a, b, c = map(int, input().split())
if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
    print(a*b*c//max(a, b, c))
else:
    print(0)