

def main():
    x_num, y_num = map(int, input().split())
    data_x = list(map(int, input().split()))
    data_y = list(map(int, input().split()))
    mod = 10 ** 9 + 7

    x_sum = 0
    for i in range(x_num):
        x_sum += (2 * i + 1 - x_num) * data_x[i]
        x_sum %= mod

    y_sum = 0
    for i in range(y_num):
        y_sum += (2 * i + 1 - y_num) * data_y[i]
        y_sum %= mod

    print((x_sum * y_sum) % mod)



if __name__ == '__main__':
    main()
