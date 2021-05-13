N,M = map(int,input().split())
D = []
for i in range(N):
    D.append(tuple(map(int, input().split())))
D.sort()

drinks=M
cost = 0
for i in D:
    if drinks > i[1]:
        drinks -= i[1]
        cost += i[1] * i[0]
    else:
        cost += (drinks * i[0])
        break

print(cost)
