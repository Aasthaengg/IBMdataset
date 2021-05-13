import math
import numpy
import sys
readline = sys.stdin.readline


def main():
    n = int(input())
    A = list(map(int, input().split()))
    avgA = numpy.average(A)
    B = list(map(lambda x: abs(x - avgA) ,A))
    minB = min(B)

    print(B.index(minB))


if __name__ == '__main__':
    main()
