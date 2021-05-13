n = int(input())
xu = []
sum_xu = 0
for i in range(n):
    x, u = input().split()
    xu.append([float(x), u])

for i in range(n):
    if xu[i][1] == 'JPY':
        sum_xu += xu[i][0]
    elif xu[i][1] == 'BTC':
        sum_xu += xu[i][0]*380000.0

print(sum_xu)
