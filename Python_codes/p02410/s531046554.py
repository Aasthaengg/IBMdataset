#!usr/bin/env python3

import sys


def main():
    m, n = [int(col_row) for col_row in sys.stdin.readline().split()]
    matrix = [[0 for col in range(n)] for row in range(m)]
    vector = [0 for row in range(n)]

    for row in range(m):
        lst = [int(element) for element in sys.stdin.readline().split()]
        for col in range(n):
            matrix[row][col] += lst[col]

    for row in range(n):
        lst = [int(element) for element in sys.stdin.readline().split()]
        vector[row] += lst[0]

    for row in range(m):
        sum_of_row = 0
        for col in range(n):
            sum_of_row += matrix[row][col] * vector[col]
        print(sum_of_row)


if __name__ == '__main__':
    main()