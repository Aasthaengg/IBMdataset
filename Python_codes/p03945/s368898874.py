def main():
    ss = input()
    put_stone = ''
    count = 0
    for stone in ss:
        if put_stone != '' and put_stone == stone:
            count += 1
        if stone == 'B':
            put_stone = 'W'
        else:
            put_stone = 'B'
    print(count)

if __name__ == '__main__':
    main()