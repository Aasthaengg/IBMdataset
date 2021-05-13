def main():
    N, A, B = (int(i) for i in input().split())
    x = min(A, B)
    y = max(0, x - (N - max(A, B)))
    print(x, y)


if __name__ == '__main__':
    main()
