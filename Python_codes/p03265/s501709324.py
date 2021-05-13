def main():
    x1, y1, x2, y2 = map(int, input().split())
    vx = x2 - x1
    vy = y2 - y1

    print(x2 - vy, y2 + vx, x1 - vy, y1 + vx)


if __name__ == "__main__":
    main()
