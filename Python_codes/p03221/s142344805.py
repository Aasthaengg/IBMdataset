n , m = map(int, input().split())

lis = []
for i in range(m):
    a = list(map(int, input().split()))
    a.append(i)
    lis.append(a)

t = 1
tmp = sorted(lis)[0][0]

nlis =[]

for i in sorted(lis):
    if tmp == i[0]:
        left = str(i[0]).zfill(6)
        right = str(t).zfill(6)
        t += 1
    else:
        t = 1
        tmp = i[0]
        left = str(i[0]).zfill(6)
        right = str(t).zfill(6)
        t += 1
    
    nlis.append([i[2],left+right])

for j in sorted(nlis):
    print(j[1])
