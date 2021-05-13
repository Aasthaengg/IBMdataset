import sys
def input(): return sys.stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    A = ['#' * (W + 2)] + ['#' + input() + '#' for _ in range(H)] + ['#' * (W + 2)]
    for i in range(H + 2):
        print(A[i])


if __name__ == "__main__":
    main()
