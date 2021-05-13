# B - Tap Dance
def main():
    s = input()
    for i in range(0,len(s)):
        if i % 2 == 0:
            if s[i] in ['R','U','D']:
                continue
            else:
                print('No')
                exit()
        else:
            if s[i] in ['L','U','D']:
                continue
            else:
                print('No')
                exit()
    print('Yes')


if __name__ == '__main__':
    main()