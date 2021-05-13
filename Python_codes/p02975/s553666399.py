import sys
from collections import Counter

input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(int, input().split()))

    c = Counter(a)
    ans = "No"
    if len(c) == 3:
        v = list(c.values())
        if v[0] == v[1] == v[2]:
            k = list(c.keys())
            if (k[0] ^ k[1] == k[2]) and (k[1] ^ k[2] == k[0]) and (k[2] ^ k[0] == k[1]):
                ans = "Yes"
    elif len(c) == 2:
        v = list(c.values())
        k = list(c.keys())
        v[0], v[1] = min(v), max(v)
        k[0], k[1] = min(k), max(k)
        if k[0] == 0 and v[0] * 2 == v[1]:
            ans = "Yes"
    elif len(c) == 1:
        k = list(c.keys())
        if k[0] == 0:
            ans = "Yes"

    print(ans)


if __name__ == "__main__":
    main()
