H, W, M = map(int, input().split())

visited = set()

h_sum = [0] * H
w_sum = [0] * W

for i in range(M):
    h, w = map(int, input().split())
    h -= 1
    w -= 1
    visited.add((h, w))
    h_sum[h] += 1
    w_sum[w] += 1

max_h = max_w = 0
can_h = []
can_w = []
for i in range(H):
    max_h = max(max_h, h_sum[i])
    
for i in range(W):
    max_w = max(max_w, w_sum[i])

for i in range(H):
    if h_sum[i] == max_h:
        can_h.append(i)
for i in range(W):
    if w_sum[i] == max_w:
        can_w.append(i)
        
ans = max_h + max_w

for i in can_h:
    for j in can_w:
        if (i, j) not in visited:
            print(ans)
            exit()

print(ans-1)