import math


def resolve():
    import sys
    import string
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    n = int(input().rstrip())
    a_list = [int(input().rstrip()) * -1 for i in range(n)]

    import numpy
    indices = numpy.argsort(a_list)
    max_num = a_list[indices[0]] * -1
    second_max_num = a_list[indices[1]] * -1

    for i in range(len(a_list)):
        if i != indices[0]:
            print(max_num)
        else:
            print(second_max_num)


if __name__ == "__main__":
    resolve()
