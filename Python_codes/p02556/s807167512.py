def e_dist_max():
    N = int(input())
    Pos_z, Pos_w = [], []  # editorial に準ずる
    for _ in range(N):
        x, y = [int(i) for i in input().split()]
        Pos_z.append(x + y)
        Pos_w.append(x - y)
    Pos_z.sort()
    Pos_w.sort()
    return max(Pos_z[-1] - Pos_z[0], Pos_w[-1] - Pos_w[0])

print(e_dist_max())