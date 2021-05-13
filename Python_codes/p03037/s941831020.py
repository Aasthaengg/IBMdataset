k, g = list(map(int, input().split()))
id = [list(map(int, input().split())) for i in range(g)]
l, r = list(zip(*id))
print(min(r) - max(l) + 1) if min(r) - max(l) >= 0 else print(0)
