import sys

def linierSearch(x,data):
    for i in range(0,len(data)):
        if data[i] == x:
            return 1
    return 0

l = []
for i in sys.stdin:
    l.append(i)

l[1] = l[1].split()
l[3] = l[3].split()

count = 0
for i in range(0,len(l[3])):
    count += linierSearch(l[3][i],l[1])

print(count)
