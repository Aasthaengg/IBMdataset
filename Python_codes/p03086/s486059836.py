def main():
    S = input()
    ans = 0
    cnt = 0
    flag = False

    for i in range(len(S)):
        if S[i] in "ACGT":
            flag = True
            cnt += 1

        if S[i] not in "ACGT" or i == len(S) - 1:
            flag = False

        if flag == False and cnt > ans:
            ans = cnt
            cnt = 0

    print(ans)


if __name__ == "__main__":
    main()
