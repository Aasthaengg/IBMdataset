time = [int(input()) for _ in range(5)]
dif = 0
dif_max = 0
for i in time:
    tmp = abs(10-int(str(i)[-1]))
    tmp = 0 if tmp == 10 else tmp
    dif += tmp
    dif_max = max(dif_max,tmp)

print(sum(time)+dif-dif_max)