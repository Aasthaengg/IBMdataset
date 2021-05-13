import sys
lines = [list(map(int, line.strip().split(' '))) for line in sys.stdin]
print(sum([1 for h,w in lines[1:] if lines[0][1] <= h and lines[0][2] <= w]))