while True:
    i = list(map(int, input().split()))
    if i[0] == 0 and i[1] == 0:
        break
    else:
        for j in range(i[0]):
            for k in range(i[1]):
                if j == 0 or j == i[0]-1:
                    print("#", end='')
                elif k == 0 or k == i[1]-1:
                    print("#", end='')
                else:
                    print(".", end='')
            print("\n", end='')
        print("\n", end='')
