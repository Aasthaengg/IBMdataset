import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

h,w,m = (int(x) for x in input().split())
rows = [[0,i] for i in xrange(h)]
cols = [[0,i] for i in xrange(w)]
bomb_dict = dict()
for i in xrange(m):
    hi,wi = (int(x)-1 for x in input().split())
    rows[hi][0] += 1
    cols[wi][0] += 1
    bomb_dict[(hi,wi)] = True

rows = sorted(rows, reverse=True)
cols = sorted(cols, reverse=True)
row_val = rows[0][0]
col_val = cols[0][0]
ans = None
for row in rows:
    if row[0] != row_val:
        break
    for col in cols:
        if col[0] != col_val:
            break
        getr = bomb_dict.get((row[1], col[1]), False)
        if not getr:
            ans = row_val + col_val
            break
    
    if ans:
        break

if ans is None:
    ans = row_val + col_val - 1
print(ans)
