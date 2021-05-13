N = int(input())
dic = {}
for i in range(N):
    S,P = map(str,input().split())
    if S not in dic:
        dic[S] = [(-1*int(P), i+1)]
    else:
        dic[S].append((-1*int(P), i+1))
ls = list(dic.items())
ls.sort()
for city in ls:
    points = sorted(city[1])
    for point in points:
        print(point[1])