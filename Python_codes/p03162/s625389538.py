import functools
import threading
import sys


def main():
    @functools.lru_cache(maxsize=None)
    def _solve(n, action):
        if n == 1:
            return Utility[1][action]
        else:
            return max(
                _solve(n - 1, a) + Utility[n][action] for a in range(3) if a != action
            )

    def solve(n):
        return max(_solve(n, a) for a in range(3))

    N = int(input())
    Utility = [[None, None, None]]
    for i in range(N):
        Utility.append([int(x) for x in input().split(" ")])
    print(solve(N))


if __name__ == "__main__":

    sys.setrecursionlimit(1024 * 1024 * 2)
    threading.stack_size(128 * 1024 * 1024 * 2)
    threading.Thread(target=main).start()
