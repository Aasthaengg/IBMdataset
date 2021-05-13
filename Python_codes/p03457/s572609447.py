T = [[0, 0]]
for i in range(int(input())):
    t, x, y = map(int, input().split())
    T.append((t, x + y))

    dt = T[i+1][0] - T[i][0]
    dxy = abs(T[i+1][1] - T[i][1])

    if dt < dxy or dt % 2 != dxy % 2:
        print("No")
        break
else:
    print("Yes")