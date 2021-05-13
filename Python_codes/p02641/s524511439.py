x, n = map(int, input().split())
ps = list(map(int, input().split()))

for i in range(x+1):
    for j in [-1, 1]:
        a = x + i * j
        if ps.count(a) == 0:
            print(a)
            exit()