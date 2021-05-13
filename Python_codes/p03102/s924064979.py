import sys
import numpy as np

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, m, c = nm()
    B = np.array(nl())
    ans = 0
    for i in range(n):
        A = np.array(nl())
        if np.sum(A * B) + c > 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
