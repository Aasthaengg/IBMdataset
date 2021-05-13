if __name__ == '__main__':
    # ??????A?????\???
    matrix = []
    matrix_size = [int(x) for x in input().split(' ')]
    for i in range(matrix_size[0]):
        matrix.append([int(x) for x in input().split(' ')])

    # ???????????????b?????\???
    vector_b = []
    for i in range(matrix_size[1]):
        vector_b.append(int(input()))

    # ??????
    result = []
    for i in range(matrix_size[0]):
        row = []
        for x, y in zip(matrix[i], vector_b):
            row.append(x*y)
        result.append(row)

    # ???????????????
    for r in result:
        print(sum(r))