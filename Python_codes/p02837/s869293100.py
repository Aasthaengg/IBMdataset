from itertools import product

N = int(input())
xy = [[] for i in range(N)]

for i in range(N):
    for j in range(int(input())):
        xy[i].append(list(map(int, input().split())))
        
ans = 0
for bit in product([0,1], repeat=N):
    f = 0
    for i, j in enumerate(bit):
        if j == 1:
            for x, y in xy[i]:
                if bit[x-1] != y:
                    f = 1
                    break
    if f == 0:
        ans = max(ans, sum(bit))
print(ans)