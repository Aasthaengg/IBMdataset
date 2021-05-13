import sys
from collections import Counter, defaultdict
import numpy as np


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    S = list(input())
    C = Counter(S)
    K = C.keys()
    answer = []
    for k in K:
        cnt = 0
        counter = []
        for s in S:
            if s == k:
                counter.append(cnt)
                cnt = 0
            else:
                cnt += 1
        counter.append(cnt)
        answer.append(max(counter))
    print(min(answer))


if __name__ == "__main__":
    main()
