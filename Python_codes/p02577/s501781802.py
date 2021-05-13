# import itertools
# import math
# import fractions
# import functools
# import copy
# from collections import deque
# from functools import reduce
# from decimal import Decimal


def main():
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])

    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
