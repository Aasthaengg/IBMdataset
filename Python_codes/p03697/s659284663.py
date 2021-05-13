def main():
    n, m = map(int, input().split())
    print(n+m) if n+m < 10 else print('error')

if __name__ == '__main__':
    main()
