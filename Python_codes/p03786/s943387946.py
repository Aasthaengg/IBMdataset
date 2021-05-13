import sys
import numpy as np

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    A = np.array(input().split(), np.int64)
    A = np.sort(A)
    Acum = np.cumsum(A)
    ans = 1
    for i in range(N-2,-1,-1):
        if Acum[i]*2 >= A[i+1]:
            ans += 1
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
