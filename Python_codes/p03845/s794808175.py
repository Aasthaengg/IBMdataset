n = int(input())
init_time = list(map(int, input().split()))
m = int(input())

drink = list()

for a in range(m):
    drink.append(list(map(int, input().split())))

x = 0

for a in range(m):
    for b in range(n):
        if drink[a][0] == b+1:
            x += drink[a][1]
        else:
            x += init_time[b]
    print(x)
    x = 0
