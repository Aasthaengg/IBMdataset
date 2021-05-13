import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()
    T = input().strip()

    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()

