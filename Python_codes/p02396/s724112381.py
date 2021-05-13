from sys import stdin

cnt = 0

while True:
    cnt += 1
    x = int(stdin.readline().rstrip())

    if x == 0:
        break

    print("Case {}: {}".format(cnt, x))

