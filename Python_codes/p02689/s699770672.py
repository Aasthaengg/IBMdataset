N, M = map(int, input().split())
H = list(map(int, input().split()))

towers = {}
for n in range(N):
    towers[n] = []

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    towers[a].append(b)
    towers[b].append(a)

result = 0
for tower_number, related_towers in towers.items():
    if len(related_towers) == 0:
        result += 1
        continue

    tower_height = H[tower_number]
    other_heights = [H[i] for i in related_towers]
    if tower_height > max(other_heights):
        result += 1

print(result)
