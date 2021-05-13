import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    vector = []
    for i in range(m):
        vector.append(int(sys.stdin.readline()))
    product = [0] * n
    for i in range(n):
        for j in range(m):
            product[i] += matrix[i][j] * vector[j]
    for i in product:
        print(i)
    return


if __name__ == '__main__':
    main()

