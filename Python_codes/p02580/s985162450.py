H, W, M = map(int, input().split())
bombs = set()

H_count = [0 for i in range(H)]
W_count = [0 for i in range(W)]

for i in range(M):
    h, w = map(lambda x:int(x) - 1, input().split())
    bombs.add((h, w))
    H_count[h] += 1
    W_count[w] += 1


A = max(H_count)
B = max(W_count)
Ah = []
Bw = []

for i, count in enumerate(H_count):
    if count == A:
        Ah.append(i)

for i, count in enumerate(W_count):
    if count == B:
        Bw.append(i)

ans = A + B
for h in Ah:
    for w in Bw:
        if (h, w) not in bombs:
            print(ans)
            exit()

print(ans - 1)
