import sys
import numpy as np


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    N = int(input())
    A = np.array(list(map(int, input().split())))
    B = np.array(list(map(int, input().split())))
    diff = A - B
    lack = -diff[diff < 0]
    enough = diff[diff > 0]
    x = lack.sum()
    enough.sort()
    enough = reversed(enough)
    s = 0
    ans = 0
    for e in enough:
        if s < x:
            s += e
            ans += 1
        else:
            break
    if s < x:
        print(-1)
    else:
        print(len(lack) + ans)


if __name__ == "__main__":
    main()
