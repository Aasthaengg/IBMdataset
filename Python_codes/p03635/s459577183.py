import sys
n,m = map(int,input().split())
if n < 2 or m < 2 or n > 100 or m > 100:
    sys.exit()

print((n-1)*(m-1))