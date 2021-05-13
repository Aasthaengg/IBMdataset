H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

color = [[-1]*W for _ in range(H)]
p, q = 0, 0
move_down_flg = 1

for i in range(N):
    for _ in range(a[i]):
        color[p][q] = i + 1
        if move_down_flg == 1 and p < H-1:
            p += 1
        elif move_down_flg == 1 and p == H-1:
            move_down_flg = 0
            q += 1
        elif move_down_flg == 0 and p > 0:
            p -= 1
        else:
            move_down_flg = 1
            q += 1

for x in color:
    print(*x)