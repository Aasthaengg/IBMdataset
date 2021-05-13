H, W, A, B = map(int, input().split(" "))

map = []
for i in range(H):
    line = []
    for j in range(W):
        if i < B and j < A or B <= i and A <= j:
            line.append('1')
        else:
            line.append('0')
    map.append(line)

print('\n'.join([''.join(m) for m in map]))