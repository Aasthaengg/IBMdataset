def main():
    a, b, c = map(int, input().split())
    print('Yes') if a + b >= c else print('No')

if __name__ == '__main__':
    main()