def print_max_min_sum(args):
    """
    args: a list of integer
    outputs a tuple

    >>> print_max_min_sum([10, 1, 5, 4, 17])
    1 17 37
    """
    print("{0} {1} {2}".format(min(args), max(args), sum(args)))


if __name__ == '__main__':
    cnt = int(input())
    nums = [int(i) for i in input().split(' ')]

    print_max_min_sum(nums[0:cnt])