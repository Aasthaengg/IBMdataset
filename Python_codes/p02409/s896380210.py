regidents = [[[0 for b in range(10)] for f in range(3) ]for r in range(4)]
n = int(input())
for i in range(n):
    building, floor, room, delta = map(int, input().split())
    regidents[building-1][floor-1][room-1] += delta
print('\n####################\n'.join('\n'.join(' '+' '.join(str(regidents[b][f][r]) for r in range(10) )for f in range(3)) for b in range(4)))