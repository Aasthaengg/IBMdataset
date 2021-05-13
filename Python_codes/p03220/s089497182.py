import sys
import numpy as np


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    t, a = nm()
    H = nl()
    T = np.array(list(map(lambda x: t - x * 0.006, H)))
    D = np.abs(a - T)
    S_i = sorted(range(0, n), key=lambda x: D[x])
    print(S_i[0] + 1)


if __name__ == '__main__':
    main()
