def main():
    S = input()
    size = len(S)
    ans = 0
    for left in range(size):
        for right in range(left, size):
            T = S[left:right + 1]
            if set(T) <= set("ACGT"):
                ans = max(ans, right - left + 1)
    print(ans)

    return


if __name__ == "__main__":
    main()
