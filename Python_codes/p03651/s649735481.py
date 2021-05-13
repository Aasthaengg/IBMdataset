import sys
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, K = in_nn()
    A = in_nl()

    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])

    if K % gcd == 0 and K <= max(A):
        ans = 'POSSIBLE'
    else:
        ans = 'IMPOSSIBLE'

    print(ans)


if __name__ == '__main__':
    main()
