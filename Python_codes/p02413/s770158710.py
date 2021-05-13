def calc_sums(tbl):
    """calculate the total sum for each row and column

    >>> calc_sums([[1, 2], [2, 1]])
    [[1, 2, 3], [2, 1, 3], [3, 3, 6]]
    """
    new_tbl = [row + [0] for row in tbl] + [[0] * (len(tbl[0])+1)]

    for i, row in enumerate(tbl):
        for j, val in enumerate(row):
            new_tbl[i][-1] += val
            new_tbl[-1][j] += val

    new_tbl[-1][-1] = sum(new_tbl[-1][:-1])

    return new_tbl


def run():
    n, m = [int(v) for v in input().split()]
    table = []

    for i in range(n):
        table.append([int(v) for v in input().split()])

    for row in calc_sums(table):
        print(" ".join([str(i) for i in row]))


run()

