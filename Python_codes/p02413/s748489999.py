rc = [int(i) for i in input().split()]
data = []

for i in range(rc[0]):
    sum_c = [int(i) for i in input().split()]
    sum_c.append(sum(sum_c))
    data += [sum_c]
    print(" ".join(map(str,sum_c)))

hoge = [[row[i] for row in data] for i in range(rc[1])]

sum_r = [sum(hoge[i]) for i in range(rc[1])]
sum_r.append(sum(sum_r))
print(" ".join(map(str,sum_r)))