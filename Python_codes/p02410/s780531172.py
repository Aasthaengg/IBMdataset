import sys

l = []
result = []
for i in sys.stdin:
    l.append(i)

for i in range(0,len(l)):
    l[i] = l[i].split()
    for j in range(0,len(l[i])):
        l[i][j] = int(l[i][j])

for i in range(1,l[0][0]+1):
    a = []
    for j in range(0,l[0][1]):
        a.append(l[i][j] * l[j+l[0][0]+1][0])
    result.append(sum(a))

for data in result:
    print(data)
