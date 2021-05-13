import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

# (int(x) for x in input().split())d.
n = int(input())
ans = 0
for a in xrange(1,n+1):
    for b in xrange(a, n+1):
        if (a*b < n):
            if (a==b):
                ans += 1
            else:
                ans += 2
        else:
            break
print(ans)
