def main():
    S = input()
    ans = 0
    cnt = 0

    for i in range(len(S)):
        if S[i] in "ACGT":
            cnt += 1

        if S[i] not in "ACGT" and cnt > ans:
            ans = cnt
            cnt = 0

        if i == len(S) - 1 and cnt > ans:
            ans = cnt
            cnt = 0

    print(ans)


if __name__ == "__main__":
    main()
