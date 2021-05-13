def main():
    S = input()
    S = S.replace("BC", "D")
    N = len(S)
    ans = 0
    a_cnt = 0
    for i in range(N):
        if S[i] == "A":
            a_cnt += 1
        elif S[i] == "D":
            ans += a_cnt
        else:
            a_cnt = 0
    print(ans)


if __name__ == '__main__':
    main()
