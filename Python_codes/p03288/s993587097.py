def main():
    r = int(input())

    if r >= 2800:
        print('AGC')
    elif r >= 1200:
        print('ARC')
    else:
        print('ABC')

if __name__ == '__main__':
    main()