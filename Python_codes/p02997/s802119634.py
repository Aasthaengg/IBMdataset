N, K = map(int, input().split())

if K > (N - 1) * (N - 2) // 2:
    print(-1)
    exit()

# N を中心とするスターグラフ
uvs = [(i, N) for i in range(1, N)]

to_decrease = (N - 1) * (N - 2) // 2 - K
for i in range(1, N):
    for j in range(i+1, N):
        if to_decrease == 0:
            break
        uvs.append((i, j))
        to_decrease -= 1
    else:
        continue
    break

print(len(uvs))
for u, v in uvs:
    print(u, v)