
def main():
    white_num, black_num = map(int, input().split())
    data = [['.' for i in range(100)] for j in range(50)] + [['#' for i in range(100)] for j in range(50)]

    black_change = black_num - 1
    count = 0
    for i in range(black_change // 25 + 1):
        high = i  * 2
        for j in range(50):
            width = j * 2
            if count == black_change:
                break
            count += 1
            data[high][width] = '#'
        if count == black_change:
            break

    black_change = white_num - 1
    count = 0
    for i in range(black_change // 25 + 1):
        high = i * 2 + 51
        for j in range(50):
            width = j * 2
            if count == black_change:
                break
            count += 1
            data[high][width] = '.'
        if count == black_change:
            break

    print(100, 100)
    for i in range(100):
        print(''.join(data[i]))


if __name__ == '__main__':
    main()

