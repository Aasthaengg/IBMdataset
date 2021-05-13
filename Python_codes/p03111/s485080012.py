def calc_mp(ls, target):
    ret = 0
    ret += 10 * (len(ls) - 1)
    val = sum(ls)
    ret += abs(val - target)
    return ret


n, a, b, c = map(int, input().split())
l_ls = []
for i in range(n):
    l_ls.append(int(input()))

pattern = []

for i in range(4 ** n):
    tmp = [0] * n
    val = i
    for j in range(n):
        tmp[j] = val % 4
        val = val // 4
    pattern.append(tmp)

ret = 10 ** 100

for item in pattern:
    if 1 not in item or 2 not in item or 3 not in item:
        continue
    else:
        ones = []
        twos = []
        threes = []
        for i in range(n):
            if item[i] == 1:
                ones.append(l_ls[i])
            elif item[i] == 2:
                twos.append(l_ls[i])
            elif item[i] == 3:
                threes.append(l_ls[i])
        mp = 0
        mp += calc_mp(ones, a)
        mp += calc_mp(twos, b)
        mp += calc_mp(threes, c)
        ret = min(ret, mp)

print(ret)
