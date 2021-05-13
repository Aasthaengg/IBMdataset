def main():
    n,a = (int(input()) for _ in range(2))
    print('Yes' if n%500 <= a else 'No')

if __name__ == '__main__':
    main()