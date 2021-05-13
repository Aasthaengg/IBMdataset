# Aizu Problem ITP_1_6_C: Official House
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


building = {b: [[0] * 10, [0] * 10, [0] * 10] for b in range(1, 5)}

N = int(input())
for k in range(N):
    b, f, r, v = [int(_) for _ in input().split()]
    building[b][f-1][r-1] += v

for b in range(1, 5):
    for level in building[b]:
        print(' ' + ' '.join([str(l) for l in level]))
    if b < 4:
        print('#' * 20)