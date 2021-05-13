from math import sin, cos, pi


def main():
    a, b, h, m = map(int, input().split())

    a_theta = (60 * h + m) * pi / 360
    b_theta = (60 * h + m) * pi / 30

    a_x = a * sin(a_theta)
    a_y = a * cos(a_theta)
    b_x = b * sin(b_theta)
    b_y = b * cos(b_theta)

    ans = ((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** 0.5

    print(ans)


if __name__ == "__main__":
    main()
