def main():
    A, B, X = map(int, input().split())
    ans = B // X - (A - 1) // X
    print(ans)


if __name__ == '__main__':
    main()
