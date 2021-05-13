def main():
    n, a, b = map(int, input().split())
    if a == b:
        print(1)
        return 0
    elif a > b or n == 1:
        print(0)
        return 0
    else:
        print((b-a)*(n-2)+1)
        return 0

if __name__ == '__main__':
    main()
