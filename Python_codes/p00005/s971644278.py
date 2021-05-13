import sys

temp = []
largest = 1

for line in sys.stdin:
    a,b = [int(x) for x in line.split()]
    if a > b:
        x,y = a,b
    else:
        x,y = b,a
    while y:
        x,y = y,x%y
    smallest = x * (a/x) * (b/x)
    print('%d %d' % (x, smallest))