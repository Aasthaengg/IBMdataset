n = int(input())
a, b = map(int, input().split())
P = list(map(int, input().split()))

p1 = 0
p2 = 0
p3 = 0

for p in P:
    if p <= a:
        p1 += 1
    elif p <= b:
        p2 += 1
    else:
        p3 += 1

print(min(p1, p2, p3))
