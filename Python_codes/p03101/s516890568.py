def main():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    a = h * w
    b = (H - h) * w
    c = (W - w) * h
    ans = H*W - (a + b + c)
    print(ans)


if __name__ == "__main__":
    main()
