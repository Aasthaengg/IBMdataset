import sys
from operator import itemgetter
read = sys.stdin.read


def main():
    N, *AB = map(int, read().split())
    A, B = zip(*sorted(zip(*[iter(AB)] * 2), key=sum, reverse=True))
    print(sum(A[::2]) - sum(B[1::2]))


if __name__ == '__main__':
    main()