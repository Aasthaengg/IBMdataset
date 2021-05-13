import math

def print_circle(r):
    """
    r: float
    outputs area and circumfence of a circle(radius r)
    
    >>> print_circle(2)
    12.566371 12.566371
    """

    print("{0:.6f} {1:.6f}".format(math.pi * r**2, 2 * math.pi * r))

if __name__ == '__main__':
    r = float(input())
    print_circle(r)