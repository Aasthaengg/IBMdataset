import threading
import sys


def main():
    def solve(n):
        if n == 1:
            return 0
        else:
            if S[n - 2] == S[n - 1]:
                return solve(n - 1)
            else:
                return solve(n - 1) + 1

    S = input()
    first_s = S[0]
    S = [1 if first_s == s else 0 for s in S]

    print(solve(len(S)))


if __name__ == "__main__":

    sys.setrecursionlimit(1024 * 1024 * 2)
    threading.stack_size(128 * 1024 * 1024 * 2)
    threading.Thread(target=main).start()
