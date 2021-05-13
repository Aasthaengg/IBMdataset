H, A = map(int, input().split())

d, m = divmod(H, A)

d += [0, 1][m != 0]
print(d)