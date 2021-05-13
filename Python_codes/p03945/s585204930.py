def main():
    S = input()
    ans = 0
    before_c = S[0]
    for c in S:
        if c != before_c:
            ans += 1
            before_c = c
    print(ans)


if __name__ == '__main__':
    main()