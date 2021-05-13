s = int(input())
ans = 0
tmp = [s]
for i in range(1, 10 ** 6 + 1):
    if tmp[i - 1] % 2 == 0:
        t = tmp[i - 1] // 2
    else:
        t = 3 * tmp[i - 1] + 1
    if tmp.count(t) != 0:
        print(i+1)
        exit(0)
    else:
        tmp.append(t)