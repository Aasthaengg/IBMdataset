# Aizu Problem ITP_1_7_C: Spreadsheet
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


n, m = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for __ in range(n)]

for row in range(n):
    A[row].append(sum(A[row]))

for row in A:
    print(' '.join([str(r) for r in row]))

last = []
for col in range(m):
    last.append(sum([A[row][col] for row in range(n)]))
last.append(sum(last))
print(' '.join([str(l) for l in last]))