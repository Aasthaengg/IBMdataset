n = int(input())
minv = 1e9+1
min_idx = -1
for i in range(n):
    a, b = map(int, input().split(' '))
    if b < minv:
        minv = b
        min_idx = a
print(min_idx+minv)
