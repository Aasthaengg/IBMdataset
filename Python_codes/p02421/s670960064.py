times = int(input())
taro_s = 0
hanako_s = 0
for i in range(times):
    taro_a, hanako_a = input().split()
    if taro_a > hanako_a:
        taro_s += 3
    elif taro_a < hanako_a:
        hanako_s += 3
    else:
        hanako_s += 1
        taro_s += 1
print(taro_s, hanako_s)