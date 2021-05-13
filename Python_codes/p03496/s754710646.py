# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc081/tasks/arc086_b

"""
import sys
from sys import stdin
input = stdin.readline


def solve(A, N):
    steps = []

    min_A = min(A)
    min_pos = A.index(min_A) + 1
    max_A = max(A)
    max_pos = A.index(max_A) + 1

    if min_A >= 0:
        steps.append([max_pos, 1])
        for i in range(2, N+1):
            steps.append([i-1, i])
    else:
       if (abs(min_A) < abs(max_A)):
           for i in range(1, N+1):
               steps.append([max_pos, i])
           steps.append([max_pos, 1])
           for i in range(2, N+1):
               steps.append([i-1, i])
       else:
           for i in range(1, N+1):
               steps.append([min_pos, i])
           steps.append([min_pos, N])
           for i in range(N, 1, -1):
               steps.append([i, i-1])
    return steps


def main(args):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = solve(A, N)
    print(len(ans))
    for x, y in ans:
        print(x, y)
#        A[y-1] += A[x-1]
#    print(*A)


if __name__ == '__main__':
    main(sys.argv[1:])
