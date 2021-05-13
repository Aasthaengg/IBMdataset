A, B = map(int, input().split())
q, r = divmod(B - 1, A - 1)
print(q + (r > 0))
