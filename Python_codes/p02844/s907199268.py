import sys
from itertools import product


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    s = input().strip().decode()
    ans = 0
    for p in product(range(10), repeat=3):
        matched = 0
        for i in range(n):
            if s[i] == str(p[matched]):
                matched += 1
            if matched == 3:
                ans += 1
                break
    print(ans)


if __name__ == "__main__":
    main()
