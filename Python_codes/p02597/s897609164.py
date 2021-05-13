import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

n = int(input())
seq = input()
r = seq.count('R')
ans = 0
if r != n and r != 0:
    cnt = 0
    for i in xrange(n):
        if seq[i] == 'R':
            cnt += 1
        else:
            ans += 1
            cnt += 1
        if cnt == r:
            break
print(ans)