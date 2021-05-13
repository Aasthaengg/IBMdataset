def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(m)]
    res = [0] * n
    for i in ab:
        res[i[0] - 1] += 1
        res[i[1] - 1] += 1
    for i in res:
        print(i)
if __name__ == '__main__':
    main()