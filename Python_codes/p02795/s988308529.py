h = int(input())
w = int(input())
n = int(input())
h, w = max(h, w), min(h, w)
black_tile = 0
for i in range(w):
    black_tile += h
    if black_tile >= n: break
print(i + 1)