a1, a2, a3 = map(int, input().split())

c1 = abs(a2 - a1) + abs(a3 - a1)
c2 = abs(a1 - a2) + abs(a3 - a2)
c3 = abs(a1 - a3) + abs(a2 - a3)

print(min(c1, c2, c3))