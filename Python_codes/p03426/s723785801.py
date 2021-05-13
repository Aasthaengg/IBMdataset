h, w, d = map(int, input().split())
# 座標記録
cords = [0] * (h*w+1)
for i in range(h):
    line = tuple(map(int, input().split()))
    for j in range(w):
        cords[line[j]] = (i, j)

# グループごとの累積和
acccosts = [0] * (h*w+1)
for num in range(1, h*w+1-d):
    nxy = cords[num]
    nnxy = cords[num+d]
    acccosts[num+d] = acccosts[num] + abs(nxy[0]-nnxy[0]) + abs(nxy[1] - nnxy[1])

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(acccosts[r] - acccosts[l])