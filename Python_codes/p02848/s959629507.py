def main():
    from string import ascii_uppercase

    N = int(input())
    S = input()

    ans = ''
    for c in S:
        new_ind = (ascii_uppercase.index(c) + N) % 26
        ans += ascii_uppercase[new_ind]

    print(ans)


if __name__ == '__main__':
    main()
