d, g = map(int, input().split())
pc_ls = []
for i in range(d):
    p, c = map(int, input().split())
    pc_ls.append([p, c])

ptns = []
for i in range(2 ** d):
    ptn = []
    for j in range(d):
        if ((i >> j) & 1):
            ptn.append(j)
    ptns.append(ptn)

ret = 10 ** 10

for item in ptns:
    cnt = 0
    pnt = 0
    for val in item:
        cnt += pc_ls[val][0]
        pnt += (100 * (val + 1)) * pc_ls[val][0] + pc_ls[val][1]
    left = g - pnt
    if left <= 0:
        ret = min(ret, cnt)
    else:
        for i in range(1, d + 1):
            if (d - i) in item:
                continue
            else:
                max_val = (100 * (d - i + 1)) * pc_ls[-i][0]
                if max_val < left:
                    cnt += pc_ls[-i][0]
                    left -= max_val
                else:
                    cnt += (left + 100 * (d - i + 1) -
                            1) // (100 * (d - i + 1))
                    break
        ret = min(ret, cnt)

print(ret)
