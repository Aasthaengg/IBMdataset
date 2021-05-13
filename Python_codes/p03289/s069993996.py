def main():
    S = input().rstrip()
    if S[0] != "A":
        print("WA")
        exit()
    if S[2:-1].count("C") != 1:
        print("WA")
        exit()
    chars = [chr(i) for i in range(97, 97+26)]
    for s in S[1:]:
        if s == "C":
            continue
        elif s not in chars:
            print("WA")
            exit()
    print("AC")


if __name__ == '__main__':
    main()
