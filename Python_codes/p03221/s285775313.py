para_line = list(map(int,input().split(' ')))
city = []
for i in range(para_line[1]):
    line = list(map(int,input().split(' ')))
    city.append(line+[i])
city.sort(key = lambda a: a[1])
city_cnt = [0 for k in range(para_line[0])]
for n in range(para_line[1]):
    city_cnt[city[n][0]-1] += 1
    city[n].append(str(city[n][0]).zfill(6)+str(city_cnt[city[n][0]-1]).zfill(6))
city.sort(key = lambda b: b[2])
for j in city:
    print(j[3])
