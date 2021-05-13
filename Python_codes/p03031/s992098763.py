import sys
import math
import itertools


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    K = [[] for _ in range(M)]

    for j in range(M):
        k = list(map(int, input().split()))
        K[j] = set(k[1:])
    P = list(map(int, input().split()))
    count = 0
    l = list(range(1, N + 1))
    for i in range(0, N + 1):
        for comb in itertools.combinations(l, i):
            flag =0
            for j in range(M):  # denkyu
                temp = set(comb)
                if len(temp.intersection(K[j]) )% 2 != P[j]:
                    flag = 1
                    break
            if flag ==0:
                count +=1
    print(count)

if __name__ == "__main__":
    main()
