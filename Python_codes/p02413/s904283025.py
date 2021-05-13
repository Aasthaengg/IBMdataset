res1  = []
r, c = [int(temp) for temp in input().split()]

for temp in range(c + 1) : res1.append(0)

for tem in range(r) :
    tem1 = [temp for temp in input().split()]
    tem2 = list(map(int, tem1))
    print(' '.join(tem1) + ' ' + str(sum(tem2)))
    for mak in range(c) :
        res1[mak] = res1[mak] + tem2[mak]
    res1[c] += sum(tem2)

res2 = list(map(str, res1))
print(' '.join(res2))