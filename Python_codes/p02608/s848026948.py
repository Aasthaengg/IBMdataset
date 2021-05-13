import itertools
from collections import defaultdict


def main():
    N = int(input())
    A = defaultdict(int)
    for x in range(1, N + 1):
        breakflag = False
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                a = x**2 + y**2 + z**2 + x * y + y * z + z * x
                if a <= N:
                    A[a] += 1
                else:
                    break
    for i in range(N):
        print(A[i + 1])


if __name__ == '__main__':
    main()
