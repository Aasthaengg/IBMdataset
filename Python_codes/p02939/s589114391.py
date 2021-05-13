def main():
    S = input()

    ans = 0
    tmp = ''
    pre = ''
    for s in S:
        tmp += s
        if tmp != pre:
            pre = tmp
            tmp = ''
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
