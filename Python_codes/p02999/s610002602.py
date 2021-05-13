import sys
input = sys.stdin.readline
def print_ans(x, a):
    """Test Case
    >>> print_ans(3, 5)
    0
    >>> print_ans(7, 5)
    10
    >>> print_ans(6, 6)
    10
    """
    if x < a:
        print("0")
    else:
        print("10")

if __name__ == '__main__':
    x, a = map(int, input().rstrip().split())
    print_ans(x, a)


