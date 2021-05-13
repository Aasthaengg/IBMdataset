import sys
from itertools import product


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    s = input().strip().decode()
    ans = 0
    for p in product(range(10), repeat=3):
        pointer = 0
        for c in map(str, p):
            while pointer < n:
                if s[pointer] == c:
                    pointer += 1
                    break
                pointer += 1
            else:
                break
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
