n, k = map(int, input().split())
h = [int(s) for s in input().split()]

total = 0

for i in range(n):
    if h[i] >= k:
        total += 1
print(total)