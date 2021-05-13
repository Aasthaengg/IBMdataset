import sys
a,b,c,d = map(int,input().split())

if not (1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100 and 1 <= d <= 100):
    sys.exit()

if ( abs(c - a) <= d*2 and abs(b - a) <= d and (c - b) <= d )or abs(c - a) <= d:
    print('Yes')
else:
    print('No')