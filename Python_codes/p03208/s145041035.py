import sys
import numpy as np

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, k = nm()
    H = [ni() for _ in range(n)]
    H = np.array(sorted(H))
    dif = H[1:] - H[:-1]
    cum_dif = np.append(0, np.cumsum(dif))
    ans = cum_dif[k - 1:] - cum_dif[:-(k - 1)]
    print(np.min(ans))


if __name__ == '__main__':
    main()
