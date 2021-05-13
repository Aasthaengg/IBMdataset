# https://kenkoooo.com/atcoder/#/contest/show/60231d3e-b3c8-4d84-87b4-3d3739b98e19

n, c, k = [int(i) for i in input().split()]

passengers = []

for _ in range(n):
    passengers.append(int(input()))

passengers = sorted(passengers)

bus = 0
cnt = 0
ptr = 0
first = None

for t in passengers:
    if cnt == 0:
        cnt = 1
        first = t
    elif cnt == c:
        cnt = 1
        first = t
        bus += 1
    elif cnt < c and t - first <= k:
        cnt += 1
    elif cnt < c and t - first > k:
        bus += 1
        first = t
        cnt = 1
else:
    if cnt > 0:
        bus += 1

print(bus)
