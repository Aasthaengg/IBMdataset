import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    M = [0] * (N - 1) + [A[-1]]
    for i in range(N - 2, -1, -1):
        M[i] = max(M[i + 1], A[i])
    cnt = 0
    maxA = 0
    for a, m in zip(A, M):
        if maxA < m - a:
            maxA = m - a
            cnt = 1
        elif maxA == m - a:
            cnt += 1
    print(cnt)






if __name__ == "__main__":
    main()
