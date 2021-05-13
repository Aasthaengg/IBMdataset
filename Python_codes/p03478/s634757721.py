import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    n, a, b = map(int, input().split())

    ans = 0
    for i in range(1, n+1):
        tmp = 0
        S = str(i)
        for s in S:
            tmp += int(s)
        if a <= tmp and tmp <= b:
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
