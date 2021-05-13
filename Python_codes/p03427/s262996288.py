n = int(input())
for i in range(9 * len(str(n)), 0, -1):
    if i <= 9:
        i_min = i
    else:
        i_min = int(str(i % 9) + '9' * (i // 9))
    if i_min <= n:
        print(i)
        exit()