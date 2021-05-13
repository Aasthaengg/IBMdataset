def main():
    S = input()
    L = len(S)
    c = S.count('0')
    print(min(c, L - c) * 2)


if __name__ == '__main__':
    main()
