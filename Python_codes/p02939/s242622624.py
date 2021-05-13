import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()

    i = 1
    prev = S[0]
    cnt = 1
    while i < len(S):
        if S[i] == prev:
            prev = prev + S[i]
            if i + 1 < len(S):
                prev = S[i] + S[i + 1]
                cnt += 1
                i += 2
            else:
                i += 1
        else:
            prev = S[i]
            cnt += 1
            i += 1

    print(cnt)


if __name__ == '__main__':
    main()
