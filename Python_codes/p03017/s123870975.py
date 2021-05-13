import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

n,a,b,c,d = (int(x) for x in input().split())
s = input()

ok1 = True
cnt = 0
for i in xrange(b,d):
    if s[i-1] == "#":
        cnt += 1
        if cnt == 2:
            ok1 = False
            break
    else:
        cnt = 0

ok2 = True
cnt = 0
for i in xrange(a,c):
    if s[i-1] == "#":
        cnt += 1
        if cnt == 2:
            ok2 = False
            break
    else:
        cnt = 0
if d > c: # a->c and b->d
    ok3 = True
else:
    cnt = 0
    ok3 = False
    for i in xrange(b-1,d+2):
        if s[i-1] == ".":
            cnt += 1
            if cnt == 3:
                ok3 = True
                break
        else:
            cnt = 0
if ok1 and ok2 and ok3:
    print("Yes")
else:
    print("No")
