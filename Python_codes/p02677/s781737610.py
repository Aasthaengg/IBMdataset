import math


def law_of_cosine(x, y, angle_between_x_y):
    rad = math.radians(angle_between_x_y)
    z = (x ** 2 + y ** 2 - 2 * x * y * math.cos(rad)) ** (1 / 2)
    return z


def main():
    a, b, h, m = map(int, input().split())

    h_angle = 30 * h + 0.5 * m
    m_angle = 6 * m
    between_angle = abs(h_angle - m_angle)
    angle = min(between_angle, 360 - between_angle)

    cm = law_of_cosine(a, b, angle)
    print(cm)


if __name__ == '__main__':
    main()