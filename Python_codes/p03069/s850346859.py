import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().rstrip()

    l_black = 0
    r_white = S.count(".")
    ans = r_white
    for i in range(N):
        if S[i] == "#":
            l_black += 1
        else:
            r_white -= 1
        count = l_black + r_white
        if count < ans:
            ans = count

    print(ans)


if __name__ == "__main__":
    main()
