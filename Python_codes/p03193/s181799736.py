n, h, w = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
print(sum([1 if a >= h and b >= w else 0 for a, b in ab]))
