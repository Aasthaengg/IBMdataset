
def main():
    a = [0 for i in range(5)]

    for i in range(3):
        x, y = map(int, input().split())
        a[x] += 1
        a[y] += 1

    flg = 1
    odd_flg = 0
    for i in range(1, 5):
        if a[i] == 0:
            flg = 0
        if a[i] % 2 == 1:
            odd_flg += 1

    if odd_flg > 2:
        flg = 0

    if flg:
        print('YES')
    else:
        print('NO')





if __name__ == '__main__':
    main()