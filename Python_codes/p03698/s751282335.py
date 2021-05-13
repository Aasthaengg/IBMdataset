import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

S = input()

if len(S) == len(set(S)):
    print('yes')
else:
    print('no')
