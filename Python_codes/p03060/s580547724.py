n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

gain = 0
for i in range(0, n):
    g = v[i] - c[i]
    if g > 0:
        gain += g

print(gain)