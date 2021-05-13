N, D = map(int, input().split())
q, r = divmod(N, 2*D + 1)
print(q + (r > 0))
