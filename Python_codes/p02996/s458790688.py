n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: x[1])

time = 0
for a, b in data:
    time += a
    if (time > b):
        print('No')
        exit()
    else:
        pass

print('Yes')
