import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    prev = ""
    l = 0
    ans = 0
    for r in range(len(S)):
        if prev != S[l:r + 1]:
            prev = S[l:r + 1]
            l = r + 1
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
