# coding: utf-8


def main():
    S = input()
    N = len(S)
    ans = 0
    if N == 1:
        ans = int(S)
    else:
        if S[1:] == "9" * (N - 1):
            ans += 1
        ans += int(S[0]) - 1
        ans += 9 * (N - 1)

    print(ans)

if __name__ == "__main__":
    main()
