a, b, c = map(int, input().split())

cnt = 0
while True:
    # print(a, b, c)
    x, y, z = a, b, c

    if x % 2 == 1 or y % 2 == 1 or z % 2 == 1:
        break

    if x == y and y == z and z == x:
        cnt = -1
        break

    x, y, z = a/2, b/2, c/2
    a, b, c = y+z, z+x, x+y
    cnt += 1
print(cnt)
