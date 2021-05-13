# vim: fileencoding=utf-8


def main():
    n = int(input())
    t, x, y = 0, 0, 0
    for i in range(n):
        a, b, c = map(int, input().split())
        d = a - t
        m = abs(x - b) + abs(y - c)
        if d - m < 0 or (d - m) % 2 == 1:
            print("No")
            return
        t, x, y = a, b, c
    print("Yes")


if __name__ == "__main__":
    main()
