def do():
    n = int(input())
    data = list(map(int, input().split()))
    datb = list(map(int, input().split()))
    sa = sum(data)
    sb = sum(datb)
    if sb < sa:
        print("No")
        return 0
    diffcnt = sb - sa
    cnt1 = 0
    cnt2 = 0
    import math
    for i in range(n):
        if data[i] > datb[i]:
            cnt1 += data[i] - datb[i]
        if data[i] < datb[i]:
            cnt2 += math.ceil((datb[i] - data[i]) / 2)
    if cnt2 <= diffcnt:
        print("Yes")
    else:
        print("No")
    #print(diffcnt, cnt1, cnt2)


do()

