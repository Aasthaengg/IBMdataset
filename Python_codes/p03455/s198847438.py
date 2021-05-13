def main():
    n, m = map(int, input().split())
    if n % 2 == 0 or m % 2 == 0:
        print('Even')
    else:
        print('Odd')
if __name__ == '__main__':
    main()