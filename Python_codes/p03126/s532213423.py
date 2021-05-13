n,m = map(int,input().split())

info = [input().split() for i in range(n)]
achi = []
for i in range(m):
    achi.append(0)

# print(info[0][0])

for i in range(n):
    for j in range(int(info[i][0])):
        num = int(info[i][j+1])
        achi[num-1] += 1


print(achi.count(n))