h, w = map(int, input().split())
lst = [[0] for _ in range(h)]
for i in range(h):
    tmp = list(input())
    lst[i] = tmp

H = [[0] * w for _ in range(h)]
W = [[0] * w for _ in range(h)]

for i in range(h):
    done = [0] * w
    for j in range(w):
        if lst[i][j] == '#':
            continue
        if done[j]:
            continue
        k = 0
        while lst[i][j+k] != '#':
            done[j+k] = 1
            k += 1  # kが照らせるマスの長さ
            if j+k > w-1:
                break
        for l in range(k):
            H[i][j+l] = k


for j in range(w):
    done = [0] * h
    for i in range(h):
        if lst[i][j] == '#':
            continue
        if done[i]:
            continue
        k = 0
        while lst[i+k][j] != '#':
            done[i+k] = 1
            k += 1  # kが照らせるマスの長さ
            if i+k > h-1:
                break
        for l in range(k):
            W[i+l][j] = k

ans = 0
for i in range(h):
    for j in range(w):
        if lst[i][j] != '#':
            ans = max(ans, H[i][j] + W[i][j] - 1)

print(ans)