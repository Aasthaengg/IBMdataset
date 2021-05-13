import sys
import math
read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, M = map(int, readline().split())
    S = readline().rstrip().decode('utf-8')
    T = readline().rstrip().decode('utf-8')

    G = math.gcd(N, M)

    A = ''.join(S[::N // G])
    B = ''.join(T[::M // G])

    if A == B:
        answer = N * M // G
    else:
        answer = -1
    print(answer)


if __name__ == '__main__':
    main()
