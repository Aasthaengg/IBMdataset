def main():
    H, W = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H)]

    ans = []
    for r, row in enumerate(A):
        for c, cell in enumerate(row):
            if c == W - 1:
                if cell & 1 and r != H - 1:
                    A[r + 1][c] += 1
                    ans.append((r, c, r + 1, c))
            else:
                if cell & 1:
                    A[r][c + 1] += 1
                    ans.append((r, c, r, c + 1))
    print(len(ans))
    for opr in ans:
        print(*map(lambda x: x + 1, opr))


if __name__ == '__main__':
    main()
