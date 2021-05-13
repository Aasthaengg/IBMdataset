def main():
    S = input().rstrip()
    v1 = int(S[:2])
    v2 = int(S[2:])
    if 1 <= v1 <= 12 and 1 <= v2 <= 12:
        print("AMBIGUOUS")
    elif 1 <= v1 <= 12 and (v2 >= 13 or v2 == 0):
        print("MMYY")
    elif (v1 >= 13 or v1 == 0) and 1 <= v2 <= 12:
        print("YYMM")
    else:
        print("NA")


if __name__ == '__main__':
    main()
