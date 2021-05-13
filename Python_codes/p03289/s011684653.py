def main():
    s = input()
    flag1, flag2, flag3 = False, False, False
    len_s = len(s)
    cnt2, cnt3 = 0, 0

    if s[0] == "A":
        flag1 = True

    for i in range(1, len_s):
        if 2 <= i <= len_s - 2 and s[i] == "C":
            cnt2 += 1
        if s[i].islower():
            cnt3 += 1

    if cnt2 == 1:
        flag2 = True

    if cnt3 == len_s - 2:
        flag3 = True

    if flag1 and flag2 and flag3:
        print("AC")
    else:
        print("WA")


if __name__ == "__main__":
    main()
