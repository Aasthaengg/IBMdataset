while True:
    height, width = [int(x) for x in input().split(" ")]
    if height == width == 0:
        break
    col1 = "#." * 150
    col2 = ".#" * 150
    col_set = col1[:width] + "\n" + col2[:width] + "\n"
    print(col_set * (height // 2) + (col1[:width] + "\n") * (height % 2))