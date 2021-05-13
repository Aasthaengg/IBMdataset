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
# print(cols)
ans = 1
for row in rows:
    ans_ans = None
    for col in cols:
        getr = bomb_dict.get((row[1], col[1]), False)
        if getr and ans_ans is None:
            ans_ans = row[0] + col[0] - 1
            # print("1",row[0],col[0], -1)
            best_ans = ans_ans
        elif getr and row[0] + col[0]-1 < ans_ans:
            best_ans = ans_ans
            break
        elif getr:
            pass
        else:
            if ans_ans is None:
                best_ans = row[0] + col[0]
                # print("2",row,col, best_ans)
            else:
                best_ans = max(row[0] + col[0], ans_ans)
                # print("3",row[0],col[0])
            break
    if best_ans > ans:
        ans = best_ans
    if best_ans < ans:
        break
    
print(ans)
