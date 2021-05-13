# AGC019B - Reverse and Compare
def main():
    S = input().rstrip()
    N = len(S)
    ans = N * (N - 1) // 2 + 1  # all possible patterns
    abc = "abcdefghijklmnopqrstuvwxyz"
    for a in abc:
        x = S.count(a)
        ans -= x * (x - 1) // 2  # exclude duplicates
    print(ans)


if __name__ == "__main__":
    main()