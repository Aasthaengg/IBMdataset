import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = [int(input()) for _ in range(N)]
A = A[::-1]


def solve():

    LIS = [A[0]]
    for i in range(1, N):

        if A[i] >= LIS[-1]:
            LIS.append(A[i])
        else:
            LIS[bisect.bisect_right(LIS, A[i])] = A[i]

    ans = len(LIS)
    print(ans)


if __name__ == '__main__':
    solve()
