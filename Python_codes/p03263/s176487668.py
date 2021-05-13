# D - Make Them Even

H, W = map(int, input().split())
A = [[0] * W for _ in range(H)]
for i in range(H):
    A[i] = list(int(x) for x in input().split())

path = []
for i in range(H):
    for j in range(W):
        if i%2 == 1:
            path.append((i, W-1-j))
        else:
            path.append((i, j))

cnt = 0
arr = []
for idx in range(len(path)-1):
    if A[path[idx][0]][path[idx][1]]%2 == 1:
        A[path[idx][0]][path[idx][1]] -= 1
        A[path[idx+1][0]][path[idx+1][1]] += 1
        cnt += 1
        arr.append((path[idx][0]+1, path[idx][1]+1, path[idx+1][0]+1, path[idx+1][1]+1))

print(cnt)
for a in arr:
    print(' '.join(map(str, a)))