import sys

input = sys.stdin.readline


def main():
    N = int(input())
    s = input().rstrip()

    n_R = s.count("R")
    n_B = s.count("B")
    if n_R > n_B:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
