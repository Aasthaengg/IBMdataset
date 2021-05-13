N = int(input())
S = [input() for T in range(0,N)]
M = int(input())
T = [input() for T in range(0,M)]
MAX = 0
for IS in set(S):
    Point = S.count(IS)-T.count(IS)
    if MAX<Point:
        MAX = Point
print(MAX)