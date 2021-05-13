import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().rstrip()

    n_w_all = S.count(".")
    n_b_all = S.count("#")
    n_w = 0
    n_b = 0
    ans = min(n_w_all, n_b_all)
    for i in range(N - 1):
        if S[i] == ".":
            n_w += 1
        else:
            n_b += 1
        num = n_b + (n_w_all - n_w)
        if num < ans:
            ans = num

    print(ans)


if __name__ == "__main__":
    main()
