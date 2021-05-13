import sys
for line in sys.stdin:
    a,b = list(map(int,line.split()))
    ab = a*b
    while b: a,b = b,a%b
    print(a,ab//a)