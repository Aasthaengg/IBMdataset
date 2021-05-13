def main():
    N = input()
    L = list(map(int, input().split()))
    a = max(L)
    b = sum(L) - a
    if a < b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()