import math
import copy

ans = 0

H, W, K = map(int, input().split())
c = []
for h in range(H):
    c.append(list(input()))

for i in range(int(math.pow(2, H+W))):
    i_bin = ''.join(list(reversed(format(i, 'b').zfill(100))))
    C = copy.deepcopy(c)
    for h in range(H):
        if i_bin[h] == '1':
            for w in range(W):
                C[h][w] = '.'
    for w in range(W):
        if i_bin[H + w] == '1':
            for h in range(H):
                C[h][w] = '.'
    count = 0
    for h in range(H):
        count += C[h].count('#')
    if count == K:
        ans += 1

print(ans)