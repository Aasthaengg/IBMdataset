import sys
input = sys.stdin.readline


def main():
    S = input().rstrip()
    rS = S[::-1]
    l = len(S)
    ans = 0
    for s1, s2 in zip(S[:l//2], rS[:l//2]):
        if s1 != s2:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
