def main():
    *L, = map(int, input().split())
    L.sort()
    print(L[0] * L[1] // 2)


if __name__ == '__main__':
    main()
