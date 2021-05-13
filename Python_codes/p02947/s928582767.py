import sys

# import bisect
# map(int, sys.stdin.read().split())
from collections import Counter



def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = []
    for i in range(N):
        s =list(input())
        s.sort()
        s = "".join(s)
        S.append(s)

    C  = Counter(S)
    ans =0
    for key,value in C.items():
        ans +=value*(value-1)/2

    print(int(ans))


if __name__ == "__main__":
    main()
