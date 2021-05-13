N, M = map(int, input().split())
X = []
Y = []
Z = []

for i in range(N):
    x, y, z = map(int, input().split())
    X += [x]
    Y += [y]
    Z += [z]

sign = [-1, 1]
ans = 0
for i in range(2):
    sx = sign[i]
    for j in range(2):
        sy = sign[j]
        for k in range(2):
            sz = sign[k]
            sum_xyz = []
            for x, y, z in zip(X, Y, Z):
                sum_xyz += [sx*x + sy*y + sz*z]
            sum_xyz = sorted(sum_xyz)[::-1]
            ans = max(ans, sum(sum_xyz[:M]))
print(ans)