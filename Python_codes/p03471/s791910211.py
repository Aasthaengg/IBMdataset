from sys import stdin
import sys

n, y = [int(i) for i in stdin.readline().rstrip().split()]

for p in range(2001):
    for q in range(n-p+1):
        r = n-p-q
        if 10000*p+5000*q+1000*r == y:
            print (str(p),str(q),str(r))
            sys.exit()

print ("-1 -1 -1")






