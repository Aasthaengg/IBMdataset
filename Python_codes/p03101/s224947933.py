def main():
    H, W = map(int, input().split(" "))
    h, w = map(int, input().split(" "))
    print((W - w) * (H - h))


if __name__ == '__main__':
    main()