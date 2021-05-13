
n, a, b = (int(x) for x in input().split())

ans = 0

# 0からnまで回す
for i in range(n + 1):
    
    # print("i : {0}".format(i))

    _sum = 0

    # 要素を1桁ずつ足していく
    for j in range(len(str(i))):

        # print("iの{0}桁目 : {1}".format(j + 1, int(str(i)[j])))

        _sum = _sum + int(str(i)[j])

        if b < _sum :
            break

    # print("sum : {0}".format(_sum))

    if a <= _sum and _sum <= b :
        ans = ans + i
        # print('追加!')

print(ans)