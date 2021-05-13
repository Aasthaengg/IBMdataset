H, W, K = map(int, input().split())
L = []
for i in range(H):
    L.append(list(input()))

counter_pattern = 0
for i in range(2 ** H):# 000~111
    for j in range(2 ** W):# 000~111
        counter_black = 0
        for h in range(H):
            for w in range(W):
                if L[h][w] == "#" and ((i >> h) & 1) == 0 and ((j >> w) & 1) == 0:
                    counter_black += 1
        if counter_black == K:
            counter_pattern += 1

print(counter_pattern)