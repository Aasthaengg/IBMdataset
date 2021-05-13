import sys
input = sys.stdin.readline
from collections import deque


def read():
    N = int(input().strip())
    S = []
    for i in range(N):
        s = input().strip()
        S.append(s)
    return N, S


def solve(N, S):
    count = 0
    for s in S:
        for j in range(len(s)):
            if s[j:j+2] == "AB":
                count += 1
    head_b = []
    tail_a = []
    for i, s in enumerate(S):
        if s[0] == "B":
            head_b.append(i)
        if s[-1] == "A":
            tail_a.append(i)
    head_b = list(sorted(head_b))
    tail_a = list(sorted(tail_a))
    if len(head_b) == 0 or len(tail_a) == 0:
        return count
    # is_same?
    if len(head_b) == len(tail_a):
        is_same = True
        for b, a in zip(head_b, tail_a):
            if b != a:
                is_same = False
                break
        if is_same:
            count -= 1
    return count + min(len(head_b), len(tail_a))


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
