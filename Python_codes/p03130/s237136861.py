G = [0] * 4
for i in range(3):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a] += 1
    G[b] += 1

for i in range(4):
    if G[i] == 3:
        print('NO')
        exit()

print('YES')
