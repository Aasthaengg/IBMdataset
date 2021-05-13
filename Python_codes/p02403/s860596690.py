while True:
    row, col = map(int,input().split(" "))
    if row == 0 and col == 0:
        break
    for i in range(row):
        print("#" * col)
    print()
