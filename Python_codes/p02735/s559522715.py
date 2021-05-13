from copy import deepcopy
from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

table = [[None] * W for _ in range(H)]
table[0][0] = (0 if S[0][0] == '.' else 1)

D = deque([(0, 0)])
new_D = deque()
while D:
    h, w = D.popleft()
    for dh, dw in ((1, 0), (0, 1)):
        if 0 <= h + dh < H and 0 <= w + dw < W and table[h + dh][w + dw] is None:
            if S[h + dh][w + dw] == S[h][w]:
                D.append((h + dh, w + dw))
                table[h + dh][w + dw] = table[h][w]
            else:
                new_D.append((h + dh, w + dw))
                table[h + dh][w + dw] = table[h][w] + 1
    if not D:
        D = deepcopy(new_D)
        new_D.clear()

print((table[H - 1][W - 1] + 1) // 2)
