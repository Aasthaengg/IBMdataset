import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    S = input().strip()
    if len(S) != 6:
        return "No"
    if S[2] == S[3] and S[4] == S[5]:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(main())
