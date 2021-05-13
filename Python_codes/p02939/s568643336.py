import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()

    prev = S[0]
    c = ""
    cnt = 1
    for s in S[1:]:
        c += s
        if prev != c:
            cnt += 1
            prev = c
            c = ""

    print(cnt)


if __name__ == '__main__':
    main()
