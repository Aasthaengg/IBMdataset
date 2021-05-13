import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

A = int(input())
B = int(input())

if A > B:
    print("GREATER")
elif A < B:
    print("LESS")
else:
    print("EQUAL")
