from collections import defaultdict, deque
import sys
#input = sys.stdin.readline
def inpl(): return list(map(int, input().split()))
N = int(input())
A = sorted(inpl())
if A[-1] < 0:
    print(A[-1] - sum(A[:-1]))
    for i in range(N-2, -1, -1):
        print(A[-1], A[i])
        A[-1] -= A[i]
else:
    print(sum(map(abs, A[1:])) - A[0])
    for i in range(N-2, 0, -1):
        a = A[i]
        if a > 0:
            print(A[0], a)
            A[0] -= a
        else:
            print(A[-1], a)
            A[-1] -= a
    print(A[-1], A[0])
