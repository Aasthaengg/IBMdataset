n = int(input())
l = list()
for i in range(n):
    l.append(list(map(int, input().split())))

l.sort(key = lambda x:x[1])

t = 0
for i in range(n):
    t += l[i][0]
    if t > l[i][1]:
        print("No")
        exit()

print("Yes")