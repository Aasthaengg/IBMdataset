import math


if __name__ == '__main__':
    radius = float(input())

    area = radius**2 * math.pi
    perimeter = 2 * radius * math.pi

    print('{0:.6f} {1:.6f}'.format(area, perimeter))