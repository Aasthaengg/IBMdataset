import sys
import itertools
sys.setrecursionlimit(10000)
def resolve():
    N, M = list(map(int, input().split(" ")))
    if N == 1 and M == 1:
        print("1")
    elif N == 1:
        print(M-2)
    elif M == 1:
        print(N-2)
    else:
        print((M-2)*(N-2))

if '__main__' == __name__:
    resolve()