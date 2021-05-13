import sys
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))

    if K > max(A):
        print("IMPOSSIBLE")
        exit()

    x = A[0]

    for i in range(1, N):
        x = math.gcd(A[i], x)

    if K % x == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
