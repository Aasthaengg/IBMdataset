import sys
a = [[str(i) for i in l.strip()] for l in sys.stdin]
print(a[0][0]+a[1][1]+a[2][2])