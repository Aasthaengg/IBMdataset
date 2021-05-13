import sys
from string import ascii_lowercase as a2z

input = sys.stdin.readline


def main():
    A = input().rstrip()

    count = {al: 0 for al in a2z}
    ans = 1
    for i, a in enumerate(A):
        ans += (i - count[a])
        count[a] += 1

    print(ans)


if __name__ == "__main__":
    main()
