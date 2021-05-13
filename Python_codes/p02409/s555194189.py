import sys

# 1????????¢10??????3????????????4?£????????????????????????????????????????
def make_room_data():
    room_data = []
    for i in range(4):
        one_house = []
        for j in range(3):
            one_floor = []
            for k in range(10):
                one_floor.append(0)

            one_house.append(one_floor)

        room_data.append(one_house)

    return room_data
    
def main():
    room_data = make_room_data()
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        data = sys.stdin.readline().strip().split(' ')
        b, f, r, v = [int(i) for i in data]
        room_data[b-1][f-1][r-1] += v

    # ????????¨???
    for i in range(4):
        for j in range(3):
            for k in range(10):
                print(' %d' % (room_data[i][j][k]), end='')

            print('')

        if i != 3:
            print('#' * 20)

if __name__ == '__main__':
    main()