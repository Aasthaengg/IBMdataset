import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    n = int(input())
    k = int(input())
    X = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += min(X[i], abs(X[i]-k))
    print(ans*2)


if __name__ == '__main__':
    main()
