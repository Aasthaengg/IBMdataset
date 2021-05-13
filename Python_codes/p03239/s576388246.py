def main():
    n, T = map(int, input().split())
    min_c = 1000
    is_able = False

    for _ in range(n):
        c, t = map(int, input().split())
        if t <= T:
            is_able = True
            if c < min_c:
                min_c = c

    if is_able:
        print(min_c)
    else:
        print("TLE")


if __name__ == "__main__":
    main()
