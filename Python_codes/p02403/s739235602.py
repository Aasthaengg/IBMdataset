while True:
    height, width = [int(x) for x in input().split(" ")]
    if height == 0 and width ==0:
        break

    for h in range(height):
        print("{0}".format("#" * width))

    print("\n", end="")