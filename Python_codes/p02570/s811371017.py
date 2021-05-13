def main(d: int, t: int, s: int):
    if d <= t*s:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    d, t, s = map(int, input().split())
    main(d, t, s)
