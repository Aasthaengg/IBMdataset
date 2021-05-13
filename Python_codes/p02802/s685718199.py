n, m = list(map(int, input().split()))
pss = [list(input().split()) for _ in range(m)]

dic = {}
for p, s in pss:
    if p not in dic:
        dic[p] = (0, 0)
    ac, wa = dic[p]
    if ac == 0 and s == 'AC':
        dic[p] = (ac + 1, wa)
    elif ac == 0 and s == 'WA':
        dic[p] = (ac, wa + 1)

dic = {k:dic[k] for k in dic if dic[k][0] == 1}

ac = sum(dic[k][0] for k in dic)
wa = sum(dic[k][1] for k in dic)
print(ac, wa)
