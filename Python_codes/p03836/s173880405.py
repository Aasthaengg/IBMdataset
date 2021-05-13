import sys
input = sys.stdin.readline
from collections import deque


def read():
    sx, sy, tx, ty = map(int, input().strip().split())
    return sx, sy, tx, ty


def solve(sx, sy, tx, ty):
    dx = tx - sx
    dy = ty - sy
    q = deque()
    q.append("U" * dy)
    q.append("R" * dx)
    q.append("D" * dy)
    q.append("L" * dx)
    q.append("L" * 1)
    q.append("U" * (dy+1))
    q.append("R" * (dx+1))
    q.append("D" * 1)
    q.append("R" * 1)
    q.append("D" * (dy+1))
    q.append("L" * (dx+1))
    q.append("U" * 1)
    return "".join(q)


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
