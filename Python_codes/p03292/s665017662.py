import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    A = sorted(nl())
    D = [A[i + 1] - A[i] for i in range(2)]
    print(sum(D))


if __name__ == '__main__':
    main()
