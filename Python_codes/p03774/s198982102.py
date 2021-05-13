n, m = map(int, input().split())
AB  = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append((a, b))

CD  =[]
for i in range(m):
    c,d = map(int, input().split())
    CD.append((c,d))

for a, b in AB:
    min_ = 10**18
    j = -1
    for i, (c, d) in enumerate(CD):
        x = abs(c-a)+abs(d-b)
        if x < min_:
            j = i+1
            min_ = x
    print(j)
