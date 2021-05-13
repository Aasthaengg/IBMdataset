ABC = list(map(int,input().split()))

ABC_sort = sorted(ABC,reverse=True)
AB = ABC_sort[0] - ABC_sort[1]
BC = ABC_sort[1] - ABC_sort[2]
time = 0
if BC % 2 == 0:
    time += BC // 2
    time += AB
else:
    AB += 1
    BC += 1
    time += BC // 2
    time += AB
print(time)