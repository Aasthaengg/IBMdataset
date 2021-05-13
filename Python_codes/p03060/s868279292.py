import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N =int(input())
    v = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ans =0
    for i in range(N):
        if v[i] >c[i]:
            ans +=v[i]-c[i]
    print(ans)

if __name__ == "__main__":
    main()
