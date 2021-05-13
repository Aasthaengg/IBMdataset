n = int(input())
l = []
for i in range(n):
    x,y = input().split()
    y = int(y)
    l.append([i+1,x,y])

l.sort(key=lambda x: (x[1],(x[2]*-1)))

for i in range(n):
    print(l[i][0])


