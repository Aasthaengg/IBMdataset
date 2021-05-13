n, h, w = map(int, input().split())
a_b = [ list(map(int, input().split())) for _ in range(n) ]

c = 0
for a, b in a_b:
    if h <= a and w <= b:
        c+=1
print(c)