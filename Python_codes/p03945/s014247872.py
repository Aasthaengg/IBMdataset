def main():
    s = input()
    print(sum([1 for i in range(len(s) - 1) if s[i] != s[i + 1]]))


if __name__ == '__main__':
    main()
