import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def f(A):
    N = len(A)
    D = {}

    for a in A:
        D[a] = D.setdefault(a, 0) + 1
    
    return sum([v * (v - 1) // 2 for v in D.values()])


def main():
    A = input().strip()

    c = f(A)

    N = len(A)
    print(N * (N - 1) // 2 - c + 1)

if __name__ == "__main__":
    main()
