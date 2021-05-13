import sys
input = sys.stdin.readline

def print_ans(A, B):
    """Test Case
    >>> print_ans(4, 12)
    16
    >>> print_ans(8, 20)
    12
    >>> print_ans(1, 1)
    2
    """
    if B % A == 0:
        print(A + B)
    else:
        print(B-A)

if __name__ == '__main__':
    A, B = map(int, input().rstrip().split())
    print_ans(A, B)


