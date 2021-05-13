# caddi2018bB - AtCoder Alloy
def main():
    N, H, W, *AB = map(int, open(0).read().split())
    ans = sum(a >= H and b >= W for a, b in zip(*[iter(AB)] * 2))
    print(ans)


if __name__ == "__main__":
    main()