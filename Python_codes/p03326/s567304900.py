import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
xyz = [[int(x) for x in input().split()] for _ in range(n)]

ans = 0

for i in range(8):
    i_bin = bin(i)[2:].zfill(3)
    new_xyz_sum = []
    for j in range(n):
        tmp = 0
        x, y, z = xyz[j]
        if i_bin[0] == "0":
            x *= -1
        if i_bin[1] == "0":
            y *= -1
        if i_bin[2] == "0":
            z *= -1
        tmp = x + y + z
        new_xyz_sum.append(tmp)
    new_xyz_sum = sorted(new_xyz_sum, reverse=True)
    ans = max(ans, sum(new_xyz_sum[:m]))

print(ans)

        
