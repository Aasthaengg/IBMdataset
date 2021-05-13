place = []
bn,fn,rn=[4,3,10]
for i in range(bn):
    place.append([])
    for j in range(fn):
        place[i].append([])
        for k in range(rn):
            place[i][j].append(0)

count = int(input())
for i in range(count):
    b,f,r,v = map(int, input().split())
    place[b-1][f-1][r-1] += v

for i in range(bn):
    for j in range(fn):
        line = ""
        for k in range(rn):
            line += " "
            line += str(place[i][j][k])
        print(line)
    if(i == bn -1):
        break
    mark = ""
    for i in range(20):
        mark += "#"
    print(mark)