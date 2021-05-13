def main():
    s = input()
    s = sorted(s)
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ans = 'None'
    for chr_alpha in ascii_lowercase:
        if chr_alpha not in s:
            ans = chr_alpha
            break
    print(ans)


if __name__ == "__main__":
    main()
