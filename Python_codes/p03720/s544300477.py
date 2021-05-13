s = input().split()

n = int(s[0])
m = int(s[1])

citys = []
for i in range(n):
    citys.append(0)


for i in range(m):
    p = input().split()
    x = int(p[0])
    y = int(p[1])
    citys[x - 1] += 1
    citys[y - 1] += 1

for i in range(len(citys)):
    print(citys[i])
