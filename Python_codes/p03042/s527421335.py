def main():
    S = input()
    first = S[:2]
    second = S[2:]
    YYMM = False
    MMYY = False

    if "00" <= first <= "99" and "01" <= second <= "12":
        YYMM = True
    if "01" <= first <= "12" and "00" <= second <= "99":
        MMYY = True

    if YYMM and MMYY:
        ans = "AMBIGUOUS"
    elif YYMM:
        ans = "YYMM"
    elif MMYY:
        ans = "MMYY"
    else:
        ans = "NA"

    print(ans)


if __name__ == "__main__":
    main()
