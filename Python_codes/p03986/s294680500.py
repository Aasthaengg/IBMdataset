import sys
input = sys.stdin.readline
from collections import deque


def read():
    X = input().strip()
    return X,


def solve(X):
    q = deque()
    for x in X:
        if x == "T":
            if len(q) > 0 and q[-1] == "S":
                # remove ST pair
                q.pop()
            else:
                q.append("T")
        elif x == "S":
            q.append("S")
    return len(q)
        


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
