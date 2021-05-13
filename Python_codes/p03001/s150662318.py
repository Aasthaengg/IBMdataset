def main():
    W, H, x, y = map(int, input().split())
    area = (H*W)/2
    mid_x, mid_y = W/2, H/2
    if x == mid_x and y == mid_y:
        ans = 1
    else:
        ans = 0
    print(area, ans)

if __name__ == "__main__":
    main()
