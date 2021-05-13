while True:
    a = list(map(lambda x : int(x), input().split(" ")))
    if a[0] == 0 and a[1] == 0:
        break

    for i,i_ in enumerate(range(a[0])):
        for j,j_ in enumerate(range(a[1])):
            if i == 0 or i == a[0] - 1 or j == 0 or j == a[1] - 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()