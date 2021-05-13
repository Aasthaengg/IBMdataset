N = int(input())
Info = [None] * 99999


# 0番の情報を持っておく
print(0)
s = input()
Info[0] = s
if s == 'Vacant':
    exit()

# N - 1番の情報を持っておく
print(N - 1)
s = input()
Info[N - 1] = s
if s == 'Vacant':
    exit()


# にぶたん
l, r = 0, N - 1
while True:
    m = (l + r) // 2

    print(m)
    s = input()
    Info[m] = s
    if s == 'Vacant':
        exit()

    if (m - l) % 2 == 0:
        if Info[m] == Info[l]:
            l = m
        else:
            r = m

    else:
        if Info[m] == Info[l]:
            r = m
        else:
            l = m
