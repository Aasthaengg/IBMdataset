a1, a2, a3 = list(map(int, input().split()))

d1 = abs(a2 - a1)
d2 = abs(a3 - a2)
d3 = abs(a1 - a3)

print(min(d1 + d2, d2 + d3, d3 + d1))