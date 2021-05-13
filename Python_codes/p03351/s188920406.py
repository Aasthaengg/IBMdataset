import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    *A, d = nm()
    a = A[0]
    c = A[2]
    A = sorted(A)
    D = [A[i + 1] - A[i] for i in range(2)]
    if all([dd <= d for dd in D]) or abs(a - c) <= d:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
