def main():
    S = input()
    T = input()
    slen = len(S)
    tlen = len(T)
    if tlen != slen + 1:
        print("No")
        return

    if T[:slen] == S:
        print("Yes")
    else:
        print("No")


main()
