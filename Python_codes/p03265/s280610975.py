def resolve():
    '''
    code here
    '''
    x1, y1, x2, y2 = [int(item) for item in input().split()]

    del_x = x2 - x1
    del_y = y2 - y1

    print(x2 - del_y, y2 + del_x, x2 - del_y - del_x, y2 + del_x - del_y)

if __name__ == "__main__":
    resolve()
