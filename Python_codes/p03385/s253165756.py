def main():
    s = input()
    cond = ''.join(sorted(s)) == 'abc'
    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
