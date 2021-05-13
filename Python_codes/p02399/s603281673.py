def print_a_b(a, b):
    """
    a: int
    b: int
    outputs quotient(int) of a and b, remainder of a and b, quotient(float) of a and b

    >>> print_a_b(3, 2)
    1 1 1.500000
    """
    print("{0} {1} {2:.6f}".format(a//b, a%b, a/b))

if __name__ == '__main__':
    (a, b) = [int(i) for i in input().split(' ')]
    print_a_b(a, b)