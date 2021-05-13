import sys

l = []
for i in sys.stdin:
    l.append(i.split())

count = 0
for i in range(1,len(l)-1):
    for j in range(0,len(l[i])):
        l[i][j] = l[i][j].lower()
    count += l[i].count(l[0][0])

print(count)
