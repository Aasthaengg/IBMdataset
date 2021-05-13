import math


def triangle(a, b, angle):
    """returns (area, circumference, height) of a triangle

    a, b: sides of a trianble
    anble: interior angle of a, b (deg)

    >>> s, l, h = triangle(4, 3, 90)
    >>> print('{:.5f} {:.5f} {:.5f}'.format(s, l, h))
    6.00000 12.00000 3.00000
    >>> s, l, h = triangle(1, 1, 60)
    >>> print('{:.5f} {:.5f} {:.5f}'.format(s, l, h))
    0.43301 3.00000 0.86603
    """
    rad = math.radians(angle)
    h = b * math.sin(rad)
    c = math.sqrt(h**2 + (a - b*math.cos(rad))**2)

    return ((a * h) / 2, a + b + c, h)


def run():
    a, b, C = [int(i) for i in input().split()]
    (area, length, height) = triangle(a, b, C)

    print(area)
    print(length)
    print(height)


if __name__ == '__main__':
    run()

