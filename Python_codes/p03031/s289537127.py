from itertools import product
N, M = map(int, input().split())
SW = []
for _ in range(M):
    k, *s = map(int, input().split())
    SW.append([*s])
p = list(map(int, input().split()))

Onoffs = product([0, 1], repeat=N)

cnt = 0
for onoff in Onoffs:
    for i, sw in enumerate(SW):
        tmp = 0
        for j in sw:
            if onoff[j-1]:
                tmp += 1
        if tmp % 2 != p[i]:
            break
    else:
        cnt += 1

print(cnt)
