import math

def main() -> None:
    a, b, h, m = map(int, input().split())

    theta = abs(30*h - 5.5*m)
    cos_theta = math.cos(math.radians(theta))
    print((a**2+b**2-2*a*b*cos_theta) ** 0.5)

    return


if __name__ == '__main__':
    main()
