def abc106b_105():
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        if i % 2 == 0: continue
        yaku_cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                yaku_cnt += 1
        if yaku_cnt == 8:
            cnt += 1

    print(cnt)


abc106b_105()
