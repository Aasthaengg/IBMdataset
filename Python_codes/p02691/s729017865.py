import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    L = defaultdict(int)
    R = defaultdict(int)
    for i in range(N):
        L[i+1+A[i]] += 1
        R[i+1-A[i]] += 1
    ans = 0
    for key, value in L.items():
        ans += value*R[key]
    print(ans)


if __name__ == '__main__':
    main()
