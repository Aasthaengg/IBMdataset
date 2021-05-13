# -*-coding:utf-8

import fileinput
import math

def main():

    m, n = map(int, input().split())

    A = [[0 for i2 in range(n)] for i1 in range(m)]

    for i in range(m):
        tokens = list(map(int, input().split()))
        for j in range(n):
            A[i][j] = tokens[j]

    b = []
    for i in range(n):
        line = input()
        b.append(int(line))

    for i in range(m):
        sum = 0
        for j in range(n):
            sum += (A[i][j] * b[j])

        print(sum)

if __name__ == '__main__':
    main()