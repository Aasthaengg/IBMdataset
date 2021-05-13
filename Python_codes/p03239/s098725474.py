def main():
    n, T = map(int, input().split())
    c_list = []

    for _ in range(n):
        c, t = map(int, input().split())
        if t <= T:
            c_list.append(c)

    if c_list:
        print(min(c_list))
    else:
        print("TLE")


if __name__ == "__main__":
    main()
