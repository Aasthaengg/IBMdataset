

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = int(input())
    x = [list(map(int, input().split())) for i in range(1)]

    count = 0
    while True:
        flg = False
        for n in range(len(x[0])):
            if x[0][n] % 2 == 1:
                flg = True
                break
            x[0][n] = x[0][n] / 2
        if flg:
            break

        count = count + 1

    print(count)
