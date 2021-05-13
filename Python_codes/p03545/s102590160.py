L = list(input())
L = [int(L[i]) for i in range(len(L))]
n = 4

for mask in range(2**n):
    total = L[0]
    s = str(L[0])
    for i in range(1, n):
        num = L[i]
        # maskのi番目にフラグが立っているかどうか
        if mask & (1 << i):
            total += num
            s += '+' + str(num)
        else:
            total -= num
            s += '-' + str(num)
    if total == 7:
        print(s+'=7')
        exit()
