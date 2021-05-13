def main():
    s = input()
    comp_num = 753
    min_diff = 754

    for i in range(len(s)-2):
        n = int(s[i:i+3])
        diff = abs(comp_num - n)
        if min_diff > diff:
            min_diff = diff

    print(min_diff)


if __name__ == "__main__":
    main()
