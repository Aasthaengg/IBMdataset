x, y = map(int, input().split(" "))


def calc():
    for i in range(1, x + 1):
        rest = x - i
        if i * 4 + rest * 2 == y or i * 2 + rest * 4 == y:
            print("Yes")
            exit()
    print("No")


calc()