def main():
    S = input()
    T = input()

    l = len(S)
    cnt = 0

    for i in range(l):
        if S[i] != T[i]:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
