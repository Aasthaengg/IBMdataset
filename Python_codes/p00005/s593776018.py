import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    n = a*b
    while b:
        a, b = b, a%b
    print(a, n//a)