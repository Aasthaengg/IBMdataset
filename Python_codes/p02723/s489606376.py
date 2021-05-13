def main():
    S = input()
    cond = S[2] == S[3] and S[4] == S[5]
    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
