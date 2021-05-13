import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    n = int(input())
    L = []
    R = []
    for _ in range(n):
        l,r = map(int, input().split())
        L.append(l)
        R.append(r)

    ans = 0
    for i in range(n):
        ans += R[i] - L[i] + 1
    print(ans)


if __name__ == '__main__':
    main()
