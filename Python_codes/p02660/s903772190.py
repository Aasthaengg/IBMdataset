n = int(input())
if n == 1:
    print(0)
else:
    cnt_ls = [0] * 41
    cnt = 0
    add = 1
    for i in range(1, 41):
        cnt_ls[i] = add
        cnt += 1
        if cnt == add + 1:
            add += 1
            cnt = 0

    f_ls = []
    tmp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            f_ls.append(cnt)
    if tmp != 1:
        f_ls.append(1)
    if f_ls == []:
        f_ls.append(1)

    ans = 0
    for i in f_ls:
        ans += cnt_ls[i]

    print(ans)
