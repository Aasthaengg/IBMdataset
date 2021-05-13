k, g = map(int, input().split())
id = [map(int, input().split()) for i in range(g)]
l, r = list(zip(*id))
print(max(min(r) - max(l) + 1, 0))
