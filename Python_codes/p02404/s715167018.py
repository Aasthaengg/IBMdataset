while True:
    height, width = [int(x) for x in input().split(" ")]
    if height == width == 0:
        break
    print("#" * width)
    column = "#" + "." * (width - 2) + "#"
    for i in range(height - 2):
        print(column)
    print("#" * width + "\n")