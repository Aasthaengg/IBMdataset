import sys
input = sys.stdin.readline
from collections import deque


def read():
    X = input().strip()
    return X,


def solve(X):
    ans = 0
    q = deque()
    for x in X:
        if x == "S":
            q.append(x)
        elif x == "T":
            if len(q) > 0:
                q.popleft()
            else:
                ans += 1
    ans += len(q)
    return ans


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
