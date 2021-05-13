N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N)]
AB.sort(key=lambda x:sum(x))

x = y = 0
i = 0
while AB:
    a,b = AB.pop()
    if i%2:
        y += b
    else:
        x += a
    i += 1
print(x-y)