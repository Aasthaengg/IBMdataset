import functools
import threading
import sys


def main():
    @functools.lru_cache(maxsize=None)
    def solve(n):
        if n == 1:
            return 0
        else:
            return min(
                solve(n - k) + abs(H[n] - H[n - k])
                for k in range(1, K + 1)
                if n - k >= 1
            )

    N, K = [int(x) for x in input().split(" ")]
    H = [None] + [int(x) for x in input().split(" ")]
    print(solve(N))


if __name__ == "__main__":

    sys.setrecursionlimit(1024 * 1024 * 2)
    threading.stack_size(128 * 1024 * 1024 * 2)
    threading.Thread(target=main).start()
