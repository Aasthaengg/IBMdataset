N, M = list(map(int, input().split()))
sides = []
for i in range(M):
    sides.append(list(map(int, input().split())))

costs = [-(10**20)]*N
costs[0] = 0

epoch = 0
update_number = 1
L = 0

while update_number > 0 and epoch < 2*(N-1):
    update_number = 0
    for side in sides:
        if costs[side[1]-1] < costs[side[0]-1]+side[2]:
            costs[side[1]-1] = costs[side[0]-1]+side[2]
            update_number += 1
    epoch += 1
    if epoch == N-1:
        L = costs[N-1]

if epoch == 2*(N-1) and L != costs[N-1]:
    print('inf')
else:
    print(costs[N-1])