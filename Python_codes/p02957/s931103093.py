def main():
    a, b = map(int, input().split())
    k = (a+b) / 2

    if k==int(k):
        print(int(k))
    else:
        print('IMPOSSIBLE')

if __name__ == '__main__':
    main()