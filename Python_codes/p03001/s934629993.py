def main():
    W, H, x, y = map(int, input().split())

    s = W * H / 2
    if x * 2 == W and y * 2 == H:
        t = 1
    else:
        t = 0
    print(s, t)


if __name__ == '__main__':
    main()
