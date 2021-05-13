import math

if __name__ == '__main__':
    pi = math.pi
    r = float(input())
    print("{0:.5f} {1:.5f}".format(pi * (r ** 2), 2 * pi * r))