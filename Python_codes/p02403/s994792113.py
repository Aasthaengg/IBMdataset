while (True):
    s = list(map(int, input().strip().split(' ')))

    if s[0] == 0 and s[1] == 0:
        break
    else:
        for i in range(s[0]):
            for j in range(s[1]):
                print("#", end="")
            print()
    print()
