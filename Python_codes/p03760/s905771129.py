import sys
input = sys.stdin.readline
from collections import deque


def read():
    O = input().strip()
    E = input().strip()
    return O, E


def solve(O, E):
    ans = []
    oq = deque(O)
    eq = deque(E)
    while eq:
        ans.append(oq.popleft())
        ans.append(eq.popleft())
    if oq:
        ans.append(oq.popleft())
    return "".join(ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
