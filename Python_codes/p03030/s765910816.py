N = int(input())
city = {}
for i in range(N):
    s,p = map(str,input().split())
    if s not in city:
        city[s] = [[int(p),i+1]]
    else:
        city[s].append([int(p),i+1])
        city[s].sort(reverse=True)

city = sorted(city.items())

for i in city:
    for j in i[1:]:
        for k in j:
            print(k[1])