import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

from collections import defaultdict
test = defaultdict(list)
test_per = defaultdict(dict)
n = int(input())
for i in xrange(n):
    nn = int(input())
    for j in xrange(nn):
        x,y = (int(x) for x in input().split())
        test[x-1].append(y)
        test_per[i][x-1] = y
ans = 0
for i in xrange(2**n):
    bini= bin(i)[2:]
    bini = '0'*(n-len(bini)) + bini
    valid = True
    for j,c in enumerate(bini):
        if c == '1':  # honnest
            for other_person in test_per[j]:
                if test_per[j][other_person] != int(bini[other_person]):
                    valid = False
                    break
        if not valid:
            break
    if valid:
        ans = max(ans, bini.count('1'))
print(ans)
            
