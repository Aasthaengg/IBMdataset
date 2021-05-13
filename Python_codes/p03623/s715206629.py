(x, a, b) = (int(tok) for tok in input().split())
dist_a = abs(x - a)
dist_b = abs(x - b)

print("A" if dist_a == min(dist_a, dist_b) else "B")