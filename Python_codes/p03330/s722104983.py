import sys
import collections
import itertools

input = sys.stdin.readline


def main():
    N, C = [int(x) for x in input().split()]
    D = [[int(x) for x in input().split()] for _ in range(C)]
    c = [[int(x) for x in input().split()] for _ in range(N)]

    A = [[] for j in range(3)]

    for j in range(N):
        for i in range(N):
            A[(i + j) % 3].append(c[j][i])

    one = collections.Counter(A[0])
    two = collections.Counter(A[1])
    three = collections.Counter(A[2])

    ans = float("inf")
    for x, y, z in itertools.permutations(range(C), 3):
        tmp = 0
        for k in one.keys():
            tmp += D[k - 1][x] * one[k]
        for k in two.keys():
            tmp += D[k - 1][y] * two[k]
        for k in three.keys():
            tmp += D[k - 1][z] * three[k]

        ans = min(ans, tmp)

    print(ans)




if __name__ == '__main__':
    main()
