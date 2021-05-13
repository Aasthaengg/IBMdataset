import sys
from itertools import product


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    m = list(map(int, input().split()))
    ans = [False] * q
    for e in product((0, 1), repeat=n):
        s = 0
        for i in range(n):
            s += e[i] * a[i]
        for i in range(q):
            if m[i] == s:
                ans[i] = True
    for a in ans:
        print("yes" if a else "no")


if __name__ == "__main__":
    main()

