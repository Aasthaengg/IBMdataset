def main():
    a, b = map(int, input().split())
    n = b - a
    if n % 2 ==0:
        ans = a + int(n/2)
        print(ans)
    else:
        print('IMPOSSIBLE')

if __name__ == '__main__':
    main()