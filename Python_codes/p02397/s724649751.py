for i in range(0, 3000):
    array = [int(x) for x in input().split(' ')]
    if array[0] == 0 and array[1] == 0:
        break
    else:
        print(' '.join([str(x) for x in sorted(array)]))
