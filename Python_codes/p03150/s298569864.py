import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    keyence = "keyence"
    S = readline().rstrip()
    for i in range(len(S)):
        for j in range(i, len(S)):
            s = "".join([S[:i], S[j:]])
            if s == keyence:
                print("YES")
                return
    print("NO")


if __name__ == '__main__':
    main()
