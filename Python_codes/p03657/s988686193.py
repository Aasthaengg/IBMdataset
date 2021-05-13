def main():
    a,b = list(map(int, input().split()))
    if a % 3 != 0 and b % 3 != 0:
        if (a+b) % 3 != 0:
            print('Impossible')
            exit()
    print('Possible')

if __name__ == '__main__':
    main()