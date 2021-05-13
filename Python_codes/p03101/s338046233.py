import sys
input = sys.stdin.readline
def print_ans(H, W, h, w):
    """Test Case
    >>> print_ans(3, 2, 2, 1)
    1
    >>> print_ans(5, 5, 2, 3)
    6
    >>> print_ans(2, 4, 2, 4)
    0
    """
    print((H - h) * (W  -w))


if __name__ == '__main__':
    H, W = map(int, input().rstrip().split())
    h, w = map(int, input().rstrip().split())
    print_ans(H, W, h, w)


