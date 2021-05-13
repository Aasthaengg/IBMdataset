import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    h, w, a, b = mi()
    g = np.zeros((h, w), dtype=int)
    g[:b, :a] = 1
    g[b:, a:] = 1
    for i in range(h):
        print(*g[i], sep='')


if __name__ == '__main__':
    main()