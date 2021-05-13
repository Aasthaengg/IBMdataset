N,M = list(map(int,input().split()))
KA = []
for i in range(N):
    KA.append(list(map(int,input().split())))

food = [0 for i in range(M)]

for i in range(N):
    x = KA[i][1:]
    for j in x:
        food[j - 1] += 1

print(food.count(N))