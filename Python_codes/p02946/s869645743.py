k,x = (int(x) for x in input().split())

list = []

for i in range(x - k + 1,x + k):
    list.append(i)

print(*list)