def main():
    r, c = [int(x) for x in input().split()]

    matrix = []
    totals = [0 for _ in range(c+1)]

    for _ in range(r):
        nums = [int(x) for x in input().split()]
        total = sum(nums)

        row = nums + [total]
        matrix.append(row)

        for i in range(c+1):
            totals[i] += row[i]

    matrix.append(totals)

    for m in matrix:
        print(" ".join([str(x) for x in m]))

if __name__ == '__main__':
    main()

