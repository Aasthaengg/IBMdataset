q = input().strip().split()
N, X, T = int(q[0]), int(q[1]), int(q[2])
ans = (N + X - 1) // X * T
print(ans)
