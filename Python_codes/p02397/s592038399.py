if __name__ == '__main__':
    while True:
        key_in = input()
        #data = key_in.split(' ')
        data = [int(x) for x in key_in.split(' ')]
        data.sort()

        if data[0] == 0 and data[1] == 0:
            break
        else:
            print('{0} {1}'.format(data[0], data[1]))