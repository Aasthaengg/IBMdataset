"""
234 23
134 14
124 14
123 23
"""
import copy
N = int(input())
initial = [list(range(1, N + 1)) for i in range(N)]

for i in range(N):
    initial[i].pop(i)
# print(initial)
neighbors = copy.deepcopy(initial)

S = sum(neighbors[-1])  # S候補の最大値

while True:
    # print(S)
    # print(neighbors)
    for i, tyouten in enumerate(neighbors):
        delta = sum(tyouten) - S
        # print(delta)
        if delta in tyouten:
            tyouten.remove(delta)
            neighbors[delta - 1].remove(i + 1)
        elif delta == 0:
            continue
        else:
            S -= 1
            neighbors = copy.deepcopy(initial)
            break
    else:
        break

# print(neighbors)

ans = []
for i, tyouten in enumerate(neighbors):
    for j in tyouten:
        if j > i+1:
            ans.append(str(i+1)+" "+str(j))

print(len(ans))
for s in ans:
    print(s)
