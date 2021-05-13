def main():
    H, W = (int(i) for i in input().split())
    h, w = (int(i) for i in input().split())
    ans = H*W - W*h - H*w + h*w
    print(ans)


if __name__ == '__main__':
    main()
