N = int(input())

seat = [0] * (N + 1)


def ask(i):
    print(i)

    s = input()
    if s == "Vacant":
        exit()
    seat[i] = s
    return s


l, r = 0, N - 1
ask(0)
ask(N - 1)

for _ in range(18):
    m = (r + l) // 2
    res = ask(m)
    if res == seat[l]:
        if (m - l) % 2 == 0:  # 席が奇数個
            l = m
        else:
            r = m
    else:
        if (m - l) % 2 == 0:  # 席が奇数個
            r = m
        else:
            l = m
