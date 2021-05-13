n = int(input())
a = sorted(map(int, input().split()))
ret = float('inf')
for p in range(1, 101):
    dist = 0
    for v in a:
        dist += (v - p) ** 2
    ret = min(ret, dist)
print(ret)