def main():
    g = [input() for _ in range(2)]
    for r in range(2):
        for c in range(3):
            if g[r][c] != g[1 - r][2 - c]:
                print('NO')
                return
    print('YES')


if __name__ == '__main__':
    main()
