from sys import stdin

while True:
    x, y = [int(x) for x in stdin.readline().rstrip().split()]
    if x == 0 and y == 0:
        break
    else:
        if x > y:
            print(y, x)
        else:
            print(x, y)

