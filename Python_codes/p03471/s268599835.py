N, Y = map(int, input().split())

# if (Y > N * 10000) or (Y < N * 1000):
#     print("{} {} {}".format(-1, -1, -1))

found = False

for x in range(N+1):
    for y in range(N+1):
        if (x + y) > N:
            continue
        z = N - x - y
        if z < 0:
            continue
        if (x * 10000 + y * 5000 + z * 1000) == Y:
            ans_x = x
            ans_y = y
            ans_z = z
            found = True

if found:
    print("{} {} {}".format(ans_x, ans_y, ans_z))
else:
    print("{} {} {}".format(-1, -1, -1))
    

