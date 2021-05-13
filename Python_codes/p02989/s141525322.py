n = int(input())
d = sorted(list(map(int, input().split())))
dl = len(d)

if not dl%2 == 0:
    print(0)
    exit()
else:
    dl_mid_1 = dl//2
    dl_mid_2 = dl_mid_1 + 1
    k_min = d[dl_mid_1 - 1]
    k_max = d[dl_mid_2 - 1]
    print(k_max - k_min)