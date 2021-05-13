import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]
    a = 0
    b = 0
    ba = 0
    za = 0

    ans = 0
    for s in S:
        if ba == 0 and s[0] == 'B' and s[-1] == 'A':
            ba = 1
        if za == 0 and s[0] != 'B' and s[-1] == 'A':
            za = 1

        ans += s.count("AB")

        if s[-1] == 'A':
            a += 1
        if s[0] == 'B':
            b += 1

    if ba == 1 and za == 0:
        print(ans + min(max(a, b) - 1, min(a, b)))
    else:
        print(ans + min(a, b))


if __name__ == '__main__':
    main()

