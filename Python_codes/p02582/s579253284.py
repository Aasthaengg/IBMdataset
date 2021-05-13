import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x = read().rstrip().decode()

def solve(x):
    if x.count('RRR'):
        return 3
    elif x.count('RR'):
        return 2
    elif x.count('R'):
        return 1
    else:
      return 0

print(solve(x))