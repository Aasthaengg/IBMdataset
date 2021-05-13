def main():
    D, T, S = map(int, input().split())
    print('Yes') if T*S>=D else print('No')


if __name__ == '__main__':
    main()