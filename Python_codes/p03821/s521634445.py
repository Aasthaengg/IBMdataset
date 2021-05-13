import sys
from math import ceil


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    A, B = [], []
    for i in range(n):
        a, b = nm()
        if a % b != 0:
            A.append(b - a % b)
        else:
            A.append(0)
        B.append(b)
    for i in range(n - 2, -1, -1):
        if A[i + 1] > A[i]:
            A[i] += B[i] * ceil((A[i + 1] - A[i]) / B[i])
    print(A[0])


if __name__ == '__main__':
    main()
